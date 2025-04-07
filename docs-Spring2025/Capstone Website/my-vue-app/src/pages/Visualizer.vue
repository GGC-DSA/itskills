<template>
  <div class="centerize">
    <h2>Job Market Overview: Click to Explore Technical & Soft Skills</h2>
    <h3> Explore a summary of the technical and soft skills generally required in each field</h3>
    <div class="chart-container">
      <div ref="chart"></div>
    </div>
  </div>
</template>


<script>
import Plotly from 'plotly.js-dist';

export default {
  name: 'SunburstChart',
  mounted() {
    this.fetchChartData();
  },
  methods: {
    async fetchChartData() {
  try {
    const response = await fetch('http://127.0.0.1:5000/sunburst'); // Fetch from Flask
    const jsonData = await response.json(); // Parse JSON response directly

    // Pass the already parsed JSON data to Plotly
    Plotly.newPlot(this.$refs.chart, jsonData.data, jsonData.layout);
  } catch (error) {
    console.error('Error fetching Sunburst chart data:', error);
  }
}
  }
};
</script>


<style scoped>
h2 {
  text-align: center;
  margin-bottom: 10px;
}
.chart-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%; /* Full width */
  height: 1000px; /* Adjust as needed */
}

</style>
