<template>
  <div class="chatbot-container">
    <h1>Job & Course Recommendations</h1>
    <h2>Input your own skills for professional and academic recommendations</h2>

    <div class="input-section">
      <label>Enter your skills (comma-separated):</label>
      <input v-model="skills" placeholder="e.g. Python, SQL, Machine Learning" />


      <button @click="getRecommendations" :disabled="loading">
        {{ loading ? "Fetching..." : "Get Recommendations" }}
      </button>
    </div>

    <div v-if="loading" class="loading">🔄 Fetching recommendations...</div>

    <div v-if="recommendation.recommended_degree" class="results-section">
      <h2>🎓 Recommended Degree: <span class="highlight">{{ recommendation.recommended_degree }}</span></h2>

      <h3>📚 Relevant Courses:</h3>
      <ul v-if="recommendation.relevant_courses.length">
        <li v-for="course in recommendation.relevant_courses" :key="course.course_name">
          <strong>{{ course.course_name }}</strong> - Hard Skills: {{ course.hard_skills.join(", ") }}
        </li>
      </ul>
      <p v-else class="no-results">No relevant courses found.</p>


      <h3>💼 Job Recommendations:</h3>
      <div v-if="recommendation.job_recommendations.length" class="jobs-list">
        <div v-for="job in recommendation.job_recommendations" :key="job.title" class="job-card">
          <h4>🔹 {{ job.title }}</h4>
          <p><strong>Required Skills:</strong> {{ job.required_skills.join(", ") }}</p>
          <details>
            <summary>Job Description</summary>
            <p>{{ job.summary }}</p>
          </details>
        </div>
      </div>
      <p v-else class="no-results">No job matches found.</p>
    </div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      skills: "",
      degree: "No Preference",
      degrees: [],  // ✅ Degrees will be fetched from Flask
      recommendation: { degree: "", courses: [], jobs: [] },
      loading: false,
    };
  },
  async created() {  // ✅ Fetch degree categories when the component is mounted
    try {
      const response = await axios.get(`${import.meta.env.VITE_API_BASE_URL}/degree_categories`);
      this.degrees = response.data.degree_categories;
    } catch (error) {
      console.error("Error fetching degree categories:", error);
    }
  },
  methods: {
    async getRecommendations() {
      if (!this.skills.trim()) {
        alert("Please enter at least one skill.");
        return;
      }

      this.loading = true;

      try {
        const response = await axios.post(`${import.meta.env.VITE_API_BASE_URL}/recommend_jobs`, {
          skills: this.skills,
          degree: this.degree,
        });

        console.log("API Response:", response.data);
        this.recommendation = response.data;
      } catch (error) {
        console.error("Error fetching recommendations:", error);
        alert("Failed to fetch recommendations. Please try again.");
      }

      this.loading = false;
    },
  },
};
</script>


<style scoped>
/* ✅ Styling for a cleaner UI */
.chatbot-container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.input-section {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 20px;
}

input, select, button {
  display: block;
  width: 100%;
  margin-top: 10px;
  padding: 10px;
  font-size: 16px;
}

button {
  background: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  margin-top: 10px;
  transition: 0.3s;
}

button:hover {
  background: #0056b3;
}

button:disabled {
  background: gray;
  cursor: not-allowed;
}

.loading {
  text-align: center;
  font-size: 18px;
  margin-top: 10px;
  color: #007bff;
}

.results-section {
  margin-top: 20px;
}

.highlight {
  color: #007bff;
  font-weight: bold;
}

.jobs-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.job-card {
  background: #e3f2fd;
  padding: 10px;
  border-radius: 8px;
}

.job-card h4 {
  margin-bottom: 5px;
}

.no-results {
  font-style: italic;
  color: gray;
}
</style>
