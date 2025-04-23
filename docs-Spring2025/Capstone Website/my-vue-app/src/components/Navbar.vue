<template>
    <nav class="navbar">
      <ul>
        <li><router-link to="/">Overview</router-link></li>
        <li><router-link to="/visualizer">All Skills Explorer</router-link></li>
        <li><router-link to="/chatbot">Path Finder</router-link></li>
        <li><router-link to="/topskills">Career Insights</router-link></li>
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
  