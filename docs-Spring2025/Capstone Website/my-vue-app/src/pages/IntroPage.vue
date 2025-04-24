<template>
  <div class="visualizer-container">
    <h1>We are Grizzly Gang</h1>
    <h2><strong>Members: Krishan, Lucas, Michelle, Nikhita</strong></h2>

    <div class="section-card">
      <h3>Intro</h3>
      <p>
        Welcome to Grizzly Paths 2025! The aim and purpose of this project is to aide IT students in deciding what courses to take and positions to pursue based upon their own input and examination of the market from real-world data brought 
        from the most popular job markets. Generated visuals and text-based responses are structured to provide with the most comprehensive recommendations based upon the user's preferences.
      </p>
    </div>

    <div class="section-card">
      <h3>General Summary</h3>
      <p>
        Our team worked toward creating a functional website that allows IT students to choose or explore job fields they desire. Based upon preferences or input from the user, the website will display relevant skills and courses required in 
        order to attain a particular job or pursue a given field of study. By web scraping contemporary records from datasets within popular job listing sites (such as LinkedIn, Glassdoor, and Indeed), vital information like descriptions, titles, 
        and primary skills were utilized by our team to create and deploy programs that give the most appropriate output to our users. Our team strives to help IT students ensure their marketability in their dream job fields by giving them direction 
        and purpose in a time of increasing choices and an ever-shifting market.
      </p>
    </div>

    <div class="section-card">
      <h3>Data</h3>
      <p>
        <strong>DISCLAIMER:</strong> Data is composed of 30,000+ records scraped from popular job listing sites (Indeed, LinkedIn, and GlassDoor) in January 2025. Much of the data was removed or ignored based upon various criteria 
        such as being missing, irregular, foreign, etc.  Vital data such as job descriptions, titles, locations, pay, and skillsets were examined, evaluated, and designed to be returned based upon user input. 
      </p>
    </div>

    <div class="section-card">
      <h3>Future Aspirations</h3>
      <p>
        There are many areas for improvement within our current build of the site. The primary area of which was making a version that incorporated a live feed of data. In other words, the data being supplied on the current build only utilizes a 
        static dataset that does not update or change as time passes - a clear weakness. In the future, if the site could be made to reference a live data feed that kept the records up-to-date and accurate, the tool would remain a much more viable 
        option for students to use.
      </p>
    </div>
    <img class="poster-container" src="../assets/Capstone-Poster.jpg"/>
  </div>
</template>

<style>
.poster-container{
  margin: 0 auto;
}
.visualizer-container {
  background-color: #fdfdfd;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  font-family: 'Segoe UI', sans-serif;
  color: #333;
}

.visualizer-container h1 {
  text-align: center;
  font-size: 2.5em;
  margin-bottom: 10px;
  color: #1a1a1a;
}

.visualizer-container h2 {
  text-align: center;
  font-size: 1.2em;
  color: #666;
  margin-bottom: 30px;
}

.section-card {
  margin-bottom: 30px;
  padding: 20px;
  background-color: #fafafa;
  border-left: 4px solid #0077cc;
  border-radius: 6px;
}

.section-card h3 {
  margin-bottom: 10px;
  font-size: 1.4em;
  color: #0077cc;
}

.section-card p {
  line-height: 1.6;
}
</style>
