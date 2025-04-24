<template>
  <div class="chatbot-container">
    <h1>Get Matched Based on Your Skills</h1>
    <h2>Enter the skills you already have or want to learn, and we’ll suggest a matching major, career paths, and relevant courses.</h2>

    <div class="input-section">
      <label>Enter your skills (comma-separated):</label>
      <input v-model="skills" placeholder="e.g. Python, SQL, Machine Learning" />


      <button @click="getRecommendations" :disabled="loading">
        {{ loading ? "Fetching..." : "Get Recommendations" }}
      </button>
    </div>

    <div v-if="loading" class="loading">🔄 Fetching recommendations...</div>

    <div v-if="recommendation.recommended_degree" class="results-section">
      <h2>Suggested Degree: <span class="highlight">{{ recommendation.recommended_degree }}</span></h2>

      <h3>Matched Courses:</h3>
      <ul v-if="recommendation.relevant_courses.length">
  <li
    v-for="course in recommendation.relevant_courses"
    :key="course.course_name"
    class="job-card"
  >
    <div class="course-title">
      <strong>{{ course.course_name }}</strong>
    </div>
    <div class="course-skills">
      Technical Skills: {{ course.hard_skills.join(", ") }}
    </div>
  </li>
</ul>

      <p v-else class="no-results">No relevant courses found.</p>


      <h3>Job Recommendations:</h3>
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
      const response = await axios.get("http://127.0.0.1:5000/degree_categories");
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
        const response = await axios.post("http://127.0.0.1:5000/recommend_jobs", {
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
  margin-bottom: 10px;
  width:90%;
  align-items: center;
  margin: 0 auto;
}

input, select, button {
  display: block;
  width: 90%;
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
  background-color: #e0f0ff;
  padding: 10px 15px;
  border-radius: 8px;
  margin-bottom: 10px;
  text-align: left;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.5;
}

.course-title {
  font-weight: bold;
  margin-bottom: 4px;
}

.course-skills {
  color: #333;
}


.job-card h4 {
  margin-bottom: 5px;
}

.no-results {
  font-style: italic;
  color: gray;
}
</style>
