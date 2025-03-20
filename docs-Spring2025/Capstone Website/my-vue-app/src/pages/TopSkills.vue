<template>
  <div>
    <h1>Top Skills for Job Roles</h1>
    
    <!-- Dropdown to select job field -->
    <select v-model="selectedJobField" @change="fetchTopSkills">
      <option v-for="jobField in jobFields" :key="jobField" :value="jobField">
        {{ jobField }}
      </option>
    </select>

    <!-- Display job titles and their skills -->
    <div v-if="Object.keys(topSkills).length">
      <h3>Job Titles and Skills</h3>
      <div v-for="(skills, jobTitle) in topSkills" :key="jobTitle" class="job-container">
        <h4 class="job-title">{{ jobTitle }}</h4>
        <ul class="skills-list">
          <li v-for="skill in skills" :key="skill" class="skill-item">{{ skill }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      jobFields: [],  // List of job fields to populate the dropdown
      selectedJobField: null,  // Selected job field
      topSkills: {},  // Object to store the top skills by job title
    };
  },
  mounted() {
    // Fetch the job fields when the component is mounted
    this.fetchJobFields();
  },
  methods: {
    async fetchJobFields() {
      try {
        const response = await fetch('http://127.0.0.1:5000/get_job_fields');
        const data = await response.json();
        this.jobFields = data;
      } catch (error) {
        console.error('Error fetching job fields:', error);
      }
    },
    async fetchTopSkills() {
      if (!this.selectedJobField) return;

      try {
        const response = await fetch('http://127.0.0.1:5000/top_skills_per_field', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ job_field: this.selectedJobField }),
        });

        const data = await response.json();
        
        // Log the response data to see its structure
        console.log('Fetched top skills:', data);

        // Check if the data is in the expected format
        if (Array.isArray(data)) {
          // Transform the data into an object where the key is the job title and the value is the list of skills
          this.topSkills = data.reduce((acc, { job_title, skills }) => {
            acc[job_title] = skills;
            return acc;
          }, {});
        }
      } catch (error) {
        console.error('Error fetching top skills:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Style for the dropdown */
select {
  margin: 20px;
  padding: 10px;
  font-size: 16px;
  width: 200px;
}

/* Style for the job containers */
.job-container {
  margin: 20px 0;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

/* Style for job title */
.job-title {
  font-size: 20px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

/* Style for the skills list */
.skills-list {
  list-style-type: none;
  padding: 0;
}

/* Style for individual skill items */
.skill-item {
  margin: 5px 0;
  font-size: 16px;
  color: #555;
}

.skill-item:hover {
  background-color: #f0f0f0;
  cursor: pointer;
}
</style>
