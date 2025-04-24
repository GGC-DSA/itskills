<template>
  <div class="centerize">
    <h2>Explore Essential Skills by Major</h2>
    <h3> View a sunburst chart showing general technical and soft skills expected in each IT field, based on real job data.</h3>
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
    const response = await fetch('https://itskills.onrender.com/sunburst'); // Fetch from Flask
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
  width: 80%; /* Full width */
  height: 800px; /* Adjust as needed */
  margin: 0 auto;
}

</style>
