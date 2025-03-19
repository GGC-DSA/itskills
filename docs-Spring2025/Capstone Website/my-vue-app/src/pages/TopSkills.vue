<template>
  <div>
    <label for="my-dropdown">Select an option:</label>
    <select id="my-dropdown" v-model="selectedValue" @change="handleSelectionChange">
      <option disabled value="">Please select one</option>
      <option v-for="option in options" :key="option.value" :value="option.value">
        {{ option.text }}
      </option>
    </select>
    <p>Selected value: {{ selectedValue }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedValue: '',
      options: [
        { text: 'Option 1', value: 'value1' },
        { text: 'Option 2', value: 'value2' },
        { text: 'Option 3', value: 'value3' },
      ],
    };
  },
  methods: {
    handleSelectionChange() {
      console.log('Selected value changed to:', this.selectedValue);
      // Perform actions based on the selected value
    },
  },
};
</script>