<template>
  <div id="app">
    <h1>Select Job Field</h1>
    <!-- Dropdown to select job field -->
    <select v-model="selectedJobField" @change="fetchChartData">
      <option disabled value="">Please select a job field</option>
      <option v-for="field in jobFields" :key="field" :value="field">{{ field }}</option>
    </select>

    <!-- Show chart when available -->
    <div v-if="chartData">
      <h2>Chart for {{ selectedJobField }}</h2>
      <img :src="`data:image/png;base64,${chartData}`" alt="Top Skills Chart" />
    </div>

    <!-- Show courses when available -->
    <div v-if="courses.length > 0">
      <h3>Recommended Courses for {{ selectedJobField }}</h3>
      <ul>
        <li v-for="course in courses" :key="course.course_name">
          <h4>{{ course.course_name }}</h4>
          <p><strong>Matching Hard Skills:</strong> {{ course.hard_skills.join(', ') }}</p>
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
        const response = await fetch("http://localhost:5000/get_job_fields");
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
        // Fetch chart data (base64 image of the chart)
        const chartResponse = await fetch("http://localhost:5000/top_skills_per_field", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            job_field: this.selectedJobField,
          }),
        });

        const chartData = await chartResponse.json();
        if (chartData.image) {
          this.chartData = chartData.image; // Assign the base64 image to `chartData`
        }

        // Fetch courses data
        const coursesResponse = await fetch("http://localhost:5000/courses_for_field", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            job_field: this.selectedJobField,
          }),
        });

        const coursesData = await coursesResponse.json();
        this.courses = coursesData; // Store the courses data in `courses`
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
  },
};
</script>

<style>
/* Add some basic styling */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  padding: 20px;
}

select {
  margin-bottom: 20px;
  padding: 10px;
}

img {
  max-width: 100%;
  height: auto;
  margin-top: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

h4 {
  margin: 10px 0;
}

p {
  margin: 5px 0;
}
</style>
