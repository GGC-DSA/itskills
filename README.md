# JobsMatch: Web/Mobile application used by IT students for matching jobs to GGC courses

## Description
This tool is designed to assist IT students in exploring different entry-level positions and then view the specific courses at GGC which would provide the entry-level skills for each position they are interested in. The scope of this project for Spring 2021 is to gather job listing datasets, clean and filter the initial datasets, manually test the project's goal, and statistically analyze data about job skills. The result of the project is that we have proven that our process works and that important job-skills data can be captured, filtered, displayed, and can be ultimately used in an application. Significant further development is required. Other IT students at GGC will have the opportunity to provide more research into different entry-level positions and provide the actual development of the Web/Mobile application to create a highly-beneficial working tool.  

### Project Demo Video: https://github.com/GGC-DSA/itskills/blob/main/media/Presentation.mp4        

## Team
Student: Hugh Smith
Advisor: Dr. Anca Doloc-Mihu, Assistant Professor of Information Technology

## Publications
* STaRS Symposium 2nd Place Poster https://ggc-stars.github.io/posters/, April 8, 2021, GGC
* CREATE Symposium, April 29, 2021, GGC

## Outreach Activities
* ITEC 2140 Introduction to Java, Profession Xin Xu, April 27, 2021
* ITEC 2140 Introduction to Java, Profession Xin Xu, April 28, 2021

## Technology
I utilized the website kaggle.com to obtain the job listing datasets, Microsoft Excel for data cleansing, Google Drive for online file location, and Google Colab Notebook for python development, data analysis, and display.
1. https://www.kaggle.com/
2. https://www.microsoft.com/en-us/microsoft-365/excel
3. https://drive.google.com/drive/my-drive  
4. https://colab.research.google.com/notebooks/intro.ipynb?utm_source=scs-index
5. Technical Results: https://github.com/GGC-DSA/itskills/blob/main/media/Technical%20Results/SD%20Skills.png

## Project Setup/Installation
1. Consulted with advisor (and searched online) to find job listing dataset sources
2. Researched online which job titles are considered entry-level within GGC IT concentrations (SD and DSA)
3. Downloaded datasets which likely contained job titles in the concentration researched
4. Created a master spreadsheet to summarize all datasets downloaded
5. Used MS Excel to explore and filter down to entry-level job titles in each dataset
   Made sure each dataset of job listings contained a column where the details
   about required skills, abilities, and responsibilities were specified by employers
6. Saved dataset copies on Google Drive
7. Saved a specific subset file for each dataset containing enough of one type of job title:
    1. For example: I created a dataset called DS-8
    2. Using excel I filtered titles down to just "Junior Software Developer" and save that file as
       "DS-8 Junior Software Developer"
8. Signed up for access to Google Colab and created the Colab notebook for this project
9. Created Python code that...
    1. Linked notebook to my Google drive
    2. Loaded single job title datasets (from step 7)
    3. Created dictionary to strip out common words during analysis
    4. Stripped meaningless characters out of data
    5. Created skill dictionaries to home in on skill words during analysis
    6. Created counter object to automatically rank top 1000 words
    7. Created analysis loop to filter out common words and filter down to skill words
    8. Created histogram plot to display skills words in a ranked order     

## Usage
1. Open up colab Notebook for project
2. Click on left side arrow buttons at each step starting from the top
    1. Run access to Google Drive at start of each session
    2. For each new dataset
        1. Run dataset load for specific subset on Google Drive
        2. Run definitions for excluding common words and garbage characters
        3. Run long list analysis of top 1000 words
        4. Run definitions for focusing in on skill-set words
        5. Run short list analysis of specific skill-sets
            1. Will print lists of skill words in different orders
            2. Will display histogram showing top skill words in chosen order

## Project Status
1.  Datasets collected and cleaned
2.  Analysis in progress
    * Implement regex to better filter job postings dataset

### To Do
1.  Collect and analyze surveys from students
2.  Build matching skills to ITEC courses
3.  Match skills from jobs to ITEC courses
4.  Build website showcase skills, courses, and job categories
5.  Figure out a way to make website interactive
