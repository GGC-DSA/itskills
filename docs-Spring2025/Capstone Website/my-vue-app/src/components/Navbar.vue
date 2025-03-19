<template>
    <nav class="navbar">
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/visualizer">Visualizer</router-link></li>
        <li><router-link to="/chatbot">Chatbot</router-link></li>
        <li><router-link to="/topskills">Top Skills</router-link></li>
      </ul>
    </nav>
  </template>
  
  <style scoped>
  .navbar {
    background-color: #333;
    padding: 10px;
    text-align: center;
  }
  
  .navbar ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    justify-content: center;
  }
  
  .navbar li {
    margin: 0 15px;
  }
  
  .navbar a {
    text-decoration: none;
    color: white;
    font-size: 18px;
  }
  
  .navbar a:hover {
    text-decoration: underline;
  }
  </style>
  