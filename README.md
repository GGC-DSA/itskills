# JobsMatch: Web/Mobile application used by IT students for matching jobs to GGC courses

## Description
This tool is designed to assist IT students in exploring different entry-level positions and then view the specific courses at GGC which would provide the entry-level skills for each position they are interested in. The scope of this project for Spring 2021 is to gather job listing datasets, clean and filter the initial datasets, manually test the project's goal, and statistically analyze data about job skills. The result of the project is that we have proven that our process works and that important job-skills data can be captured, filtered, displayed, and can be ultimately used in an application. Significant further development is required. Other IT students at GGC will have the opportunity to provide more research into different entry-level positions and provide the actual development of the Web/Mobile application to create a highly-beneficial working tool.  

## Project Demo Video
### Fall '23: [Fall 2023 Presentation](https://github.com/GGC-DSA/itskills/assets/60529957/c88c3360-a92b-4571-852c-53548882d7f2)
### Spring '23:  [Grizzly Insights Screencast](https://github.com/GGC-DSA/itskills/blob/main/media/Spr%20'23/ItSkills%20Screencast%20Spring%202023.mp4)
### Summer '21: [Hugh Smith Presentation](https://github.com/GGC-DSA/itskills/blob/main/media/Sum%20'21/Presentation.mp4)

## Project Website 
### Spring '23: [Grizzly Path](ggc-dsa.github.io/itskills/)

## Notebook
### Fall '23: [Fall 2023 Notebook](https://github.com/GGC-DSA/itskills/blob/main/Fall%202023/Notebook/EditingCSV.ipynb)

### Spring '23: [Grizzly Insights Notebook](https://github.com/GGC-DSA/itskills/blob/main/Spr%20'23/Grizzly_Insights.ipynb)

## Final Report
### Fall '23: [Fall 2023 Final Report](https://github.com/GGC-DSA/itskills/blob/main/Fall%202023/Report/Fall_2023_Report.pdf)
### Spring '23: [Grizzly Insights Final Report](https://github.com/GGC-DSA/itskills/blob/main/Spr%20'23/Grizzly%20Insights%20Final%20Report.pdf)

## Fall '23 Team
* Students: Sam Downs
* Advisor: Dr. Anca Doloc-Mihu

## Spring '23 Team
![alt text](https://github.com/GGC-DSA/itskills/blob/main/media/Spr%20'23/Team%20Photo)
* Students: Anel Coralic, Sam Downs, Ashley Mendez
* Advisor: Dr. Anca Doloc-Mihu, Assistant Professor of Information Technology

## Spring '22 Team
* Student: Michael Murillo Martinez
* Advisor: Dr. Anca Doloc-Mihu, Assistant Professor of Information Technology

## Summer '21 Team
* Student: Hugh Smith
* Advisor: Dr. Anca Doloc-Mihu, Assistant Professor of Information Technology

## Publications
### STaRS Symposium Poster
* [Grizzly Insights Poster, April 13, 2023 at GGC](https://github.com/GGC-DSA/itskills/blob/main/media/Spr%20'23/Grizzly_Insight_STARS_Poster_1.pdf)
* 2nd Place Poster https://ggc-stars.github.io/posters/, April 8, 2021 at GGC
### CREATE Symposium
* [Grizzly Insights Presentation, April 27, 2023 at GGC](https://github.com/GGC-DSA/itskills/blob/main/media/Spr%20'23/Grizzly%20Insights%20CREATE_Presentation_ITSkills.pptx)
* CREATE Symposium, April 29, 2021, GGC

## Outreach Activities
* ITEC 2140 Introduction to Java, Profession Xin Xu, April 27, 2021
* ITEC 2140 Introduction to Java, Profession Xin Xu, April 28, 2021

## Technology
### Fall '23
* [Jupyter Notebook](https://jupyter.org/install)
* Python, JavaScript, JSON
### Spring '23
* [Web Scraper Google Chrome Extension](https://chrome.google.com/webstore/detail/web-scraper-free-web-scra/jnhgnonknehpejjnehehllkliplmbmhn?hl=en)
* [Web Scraper YouTube Tutorial](https://youtu.be/aClnnoQK9G0)
* [Jupyter Notebook](https://jupyter.org/install)
* [Google Colab](https://colab.research.google.com/)
* Python, HTML, JavaScript, CSS
### Summer '21
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
    5. Created counter object to automatically rank top 1000 words
    6. Created dictionaries to home in on select words during analysis
        * Created MS Excel file "SD Key Skills Python Dictionary Builder"
        * Copied Top 1000 words/ranks from Python results to this file
        * Worked through list to create common word and skill set dictionaries
        * Formatted to put back into Python coding to build dictionaries
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
1.  Datasets collected from Jan '23
2.  Cleaned and Analyzed for common skills and job titles
3.  Grizzly Path Website up to date since April '23

## Datasets
### Fall 2023
* [Cleaned Skills Survey](https://github.com/GGC-DSA/itskills/blob/main/Fall%202023/Documents/IT_Skills_Survey.csv)
* [Not Cleaned Skills Survey](https://github.com/GGC-DSA/itskills/blob/main/Fall%202023/Documents/Matching_Skills_Courses_3_16_2023_11.32.csv)
* [Skills To Classes](https://github.com/GGC-DSA/itskills/blob/main/Fall%202023/Documents/CoursesToSkills.csv)
* [Skills To List of Classes](https://github.com/GGC-DSA/itskills/blob/main/Fall%202023/Documents/CoursesToSkillsList.csv)
### Cleaned
* [Digital Media](https://github.com/GGC-DSA/itskills/blob/main/Spr%20'23/Combined%2C%20Compressed%2C%20and%20Generalized/DMDF.csv)
* [Enterprise Systems](https://github.com/GGC-DSA/itskills/blob/main/Spr%20'23/Combined%2C%20Compressed%2C%20and%20Generalized/ESDF.csv)
* [Systems and Security](https://github.com/GGC-DSA/itskills/blob/main/Spr%20'23/Combined%2C%20Compressed%2C%20and%20Generalized/SASDF.csv)
* [Software Development](https://github.com/GGC-DSA/itskills/blob/main/Spr%20'23/Combined%2C%20Compressed%2C%20and%20Generalized/SDDF.csv)
* [Data Science and Analytics](https://github.com/GGC-DSA/itskills/blob/main/Spr%20'23/Anel's%20DSA/cleanedDSAData.csv)
### Original
* [Indeed CSV files](https://github.com/GGC-DSA/itskills/tree/main/Spr%20'23/Indeed%20Datasets)
* [Simply Hired CSV files](https://github.com/GGC-DSA/itskills/tree/main/Spr%20'23/SimplyHiredData)

## Main methods for Analysis, ML/AI 
* Python - value_counts()
* Predicting job titles - Naive Byes, Logistic Regression, Support Vector Machine, Random Forest

## 2 Main Results
![Systems and Security Common Job Titles](https://github.com/GGC-DSA/itskills/blob/main/media/Spr%20'23/Systems%20and%20Security%20Results/SAS_Common_JobTitles.jpg)
![Software Developer Common Skills for Web Developer](https://github.com/GGC-DSA/itskills/blob/main/media/Spr%20'23/Software%20Development%20Results/SD_CommonSkills_WebDeveloper.jpg)

### Fall 2023 Remaining Scope
1. Create/Update GGC class survey and ask collect data from students using the survey.
2. Collect more information about Entriprise Systems Classes.
3. Add a disclaimer page
4. Refactor the TreeCreation.js file

### Spring 2022 Remaing Scope of Project
1. Create/Update GGC class survey. Needs to be user friendly and easier to extract data.
2. Ask GGC IT students to complete survey
3. Associate skills from job titles to GGC courses.
4. Update Grizzly Path website with GGC courses 

