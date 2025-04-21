<template>
  <div id="app">
    <h1>Determine Top Skills Per Field</h1>
    <h2>View live representations of the most-demanded skills in the most prominent positions on the market right now</h2>
    <h2>Select Job Field</h2>
    <!-- Dropdown to select job field -->
    <select v-model="selectedJobField" @change="fetchChartData">
      <option disabled value="">Please select a job field</option>
      <option v-for="field in jobFields" :key="field" :value="field">{{ field }}</option>
    </select>

    <!-- Show chart when available -->
    <div v-if="chartData">
  <h2>Chart for {{ selectedJobField }}</h2>
</div>

<div class="chart-description-wrapper">
  <div class="chart-container" ref="plotContainer" style="width: 100%; height: 800px;"></div>

  <div class="description-container">
    <h3>What You’re Seeing</h3>
    <p>
      These charts display the top 5 job titles within the selected field, each branching into the top 5 most relevant skills based on real job descriptions.
    </p>
    <p>
      These skills are extracted from live job market data and mapped to recommended courses that cover those skills — helping you understand what’s in demand and how to prepare for it.
    </p>
    <p>
      Use this visualization to explore and compare different IT domains, and to discover which skills and courses will help you break into your desired field.
    </p>
  </div>
</div>


    <!-- Show courses when available -->
    <div v-if="courses.length > 0">
      <h3>Recommended Courses for {{ selectedJobField }}</h3>
      <ul class="course-list">
        <li v-for="course in courses" :key="course.course_name" class="course-card">
          <h4 class="course-name">{{ course.course_name }}</h4>
          <p class="course-skills"><strong>Matching Hard Skills:</strong> {{ course.hard_skills.join(', ') }}</p>
        </li>
      </ul>
    </div>

    <!-- Display message if no courses are found -->
    <div v-else-if="selectedJobField && courses.length === 0">
      <p>No courses found for the selected job field.</p>
    </div>
  </div>
</template>

<script>
import Plotly from 'plotly.js-dist';
export default {
  data() {
    return {
      selectedJobField: "",      // Store the selected job field
      jobFields: [],             // Will store job fields dynamically from the backend
      chartData: null,           // Will store the base64 image data for the chart
      courses: [],               // Will store courses for the selected job field
    };
  },
  created() {
    this.fetchJobFields(); // Fetch job fields when the component is created
  },
  methods: {
    // Fetch job fields from the backend
    async fetchJobFields() {
      try {
        const response = await fetch("http://127.0.0.1:5000/get_job_fields");
        const data = await response.json();
        this.jobFields = data; // Assign fetched job fields to the `jobFields` array
      } catch (error) {
        console.error("Error fetching job fields:", error);
      }
    },

    // This method will be triggered when the user selects a job field
    async fetchChartData() {
  if (!this.selectedJobField) return;

  try {
    // Fetch chart JSON data
    const chartResponse = await fetch("http://127.0.0.1:5000/top_skills_per_field", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        job_field: this.selectedJobField,
      }),
    });

    const chartData = await chartResponse.json();
    this.chartData = chartData; // Store the chart JSON data for conditional rendering

    // Plot the sunburst chart
    this.$nextTick(() => {
      Plotly.newPlot(this.$refs.plotContainer, chartData.data, chartData.layout);
    });

    // Fetch courses data
    const coursesResponse = await fetch("http://127.0.0.1:5000/courses_for_field", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        job_field: this.selectedJobField,
      }),
    });

    const coursesData = await coursesResponse.json();
    this.courses = coursesData;

  } catch (error) {
    console.error("Error fetching data:", error);
  }
},
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  padding: 20px;
}

select {
  margin-bottom: 20px;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

img {
  max-width: 100%;
  height: auto;
  margin-top: 20px;
}
.chart-description-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: flex-start;
  gap: 30px;
  margin-top: 40px;
}

.chart-container {
  flex: 2; 
}

.description-container {
  flex: 1; 
  padding: 20px;
  background-color: #f9f9f9;
  border-left: 4px solid #0077cc;
  border-radius: 6px;
  font-family: 'Segoe UI', sans-serif;
  line-height: 1.6;
}


.course-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.course-card {
  background: white;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.course-card:hover {
  transform: translateY(-5px);
  box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.15);
}

.course-name {
  font-size: 18px;
  font-weight: bold;
  color: #007bff;
  margin-bottom: 10px;
}

.course-skills {
  font-size: 14px;
  color: #666;
  margin-top: 5px;
}

h1 {
  font-size: 24px;
  color: #333;
}

h2, h3 {
  font-size: 20px;
  color: #555;
}

p {
  font-size: 16px;
  color: #777;
}
</style>
