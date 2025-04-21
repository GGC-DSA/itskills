<template>
  <div class="visualizer-container">
    <Navbar />
    <router-view></router-view>
    <Watermark>
    <img class="logo-watermark" src="./assets/ggc logo.png" alt="Logo" />
  </Watermark>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import { ref } from 'vue';
import { Watermark } from '@watermarkify/vue-watermark';



export default {
  components: {
    Navbar
  }
}
</script>

<style>
.visualizer-container {
  text-align: center;
  padding: -20px;
  background-image: url('./assets/ggc_background_blurred.png');
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}

.logo-watermark {
  position: absolute; /* Position the logo absolutely */
  top: 20px;  /* Distance from the top */
  right: 30px; /* Distance from the right */
  width: 15%;  /* Adjust the width as needed */
  height: auto;  /* Maintain aspect ratio */
}
</style>
