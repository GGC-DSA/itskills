from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin  # ✅ Import CORS
import plotly.express as px
import pandas as pd
import json
import re
import random
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import base64
from io import BytesIO
import textwrap
import pickle
from flask import send_from_directory
import os
def load_job_data(pkl_path='job_data.pkl'):
    with open(pkl_path, 'rb') as f:
        all_jobs_df, skills_by_domain = pickle.load(f)
    return all_jobs_df, skills_by_domain

app = Flask(__name__)
CORS(app)  

# ========== Load Data Once (Global Variables) ========== #
combined_df = pd.read_json('updated_combined_df.json', orient='records')
df = pd.read_csv("merged_jobs_with_degrees_and_skills.csv")

# Define acceptable seniority levels
valid_seniority = {"Associate", "Entry level", "Internship", "Not Applicable", ""}
df = df[df["job_seniority_level"].fillna("").isin(valid_seniority)]  # ✅ Filter once

# Keep only relevant columns
df = df[["job_title", "job_summary", "extracted_skills", "degree_category"]]

# Remove listings with 0-3 skills
df["skill_count"] = df["extracted_skills"].apply(lambda x: len(str(x).split(',')))
df = df[df["skill_count"] > 3].drop(columns=["skill_count"])

# Normalize skills: Convert to lowercase, strip spaces
all_skills = [
    skill.strip().lower()
    for skills in df["extracted_skills"].dropna()
    for skill in skills.split(',')
]

# Get unique top 100 skills
skill_counts = Counter(all_skills)
top_100_skills = list(dict(skill_counts.most_common(100)).keys())

# Load courses from JSON file
with open("compiled_courses.json", "r") as f:
    course_data = json.load(f)

# ========== Flask Routes ========== #

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Catch-all route for Vue SPA
@app.route('/<path:path>')
def catch_all(path):
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/sunburst')
def sunburst_chart():
    fig = px.sunburst(
        combined_df,
        path=['Domain', 'Category', 'Keyword'],
        values='Count',
        title='Job Market Overview: Click to Explore Technical, Soft, & PM Skills',
        color='Domain',
        color_discrete_sequence=px.colors.qualitative.Pastel,
        branchvalues='total'
)

    fig.update_traces(
        textinfo='label',
        textfont_size=12,
        insidetextorientation='radial',
        marker=dict(line=dict(color='white', width=2)),
        maxdepth=2  # Only Domain & Category visible at first
)

    fig.update_layout(
        margin=dict(t=50, l=0, r=0, b=0),
        width=800, height=800,
        title_x=0.5,
        title_font_size=24
)

    return jsonify(json.loads(fig.to_json()))

# ========== Chatbot API Routes ========== #

# Function to clean job titles
def clean_title(title):
    return re.split(r"[-(]", title, 1)[0].strip()

# Function to get relevant courses
def get_courses(degree_category, user_skills):
    user_skills = {skill.strip().lower() for skill in user_skills}
    
    # Filter courses by major
    courses = [(name, attr) for name, attr in course_data.items() if attr["major"] == degree_category]

    categorized_courses = {"1000": [], "2000": [], "3000": [], "4000": []}
    matched_courses = []

    for course_name, attributes in courses:
        match = re.search(r"(\d{4})", course_name)
        if match:
            level = match.group(1)[0] + "000"
            if level in categorized_courses:
                categorized_courses[level].append((course_name, attributes))

        course_skills = {skill.strip().lower() for skill in attributes["hard_skills"]}

        if any(user_skill in course_skill for course_skill in course_skills for user_skill in user_skills):
            matched_courses.append((course_name, attributes))

    print(f"Matched Courses: {matched_courses}")

    if not matched_courses:
        all_courses = [course for level in categorized_courses.values() for course in level]
        matched_courses = random.sample(all_courses, min(3, len(all_courses)))

    print(f"Final Selected Courses: {matched_courses}")
    
    return matched_courses[:3]


def calculate_weight(user_skills, courses):
    major_scores = {}

    for course, data in courses.items():
        # go through each course and extract their skills
        major = data['major']
        course_skills = set(data['hard_skills'])
        course_skills=[skill.lower() for skill in course_skills]
        
        #see what skills match for each course
        matched_skills = set(user_skills).intersection(course_skills)
        
        
        # proportional weight based on matched skills
        weight = len(matched_skills) / len(course_skills) if course_skills else 0
        
        # add the weights for each major
        if major not in major_scores:
            major_scores[major] = 0
        major_scores[major] += weight

    # Find the major with the highest total score
    best_major = max(major_scores, key=major_scores.get)
    return best_major

@app.route('/recommend_jobs', methods=['POST'])
def recommend_jobs():
    data = request.get_json()
    user_skills = {skill.strip().lower() for skill in data.get("skills", "").split(',')}
    selected_degree = data.get("degree", "No Preference")

    job_matches = []

    for _, row in df.iterrows():
        if selected_degree != "No Preference" and row["degree_category"] != selected_degree:
            continue  

        skills_list = {skill.strip().lower() for skill in str(row["extracted_skills"]).split(',')}
        matched_skills = user_skills & skills_list  

        if matched_skills:
            proportion = len(matched_skills) / len(skills_list)
            job_matches.append((clean_title(row["job_title"]), row["job_summary"], proportion, row["degree_category"], row["extracted_skills"]))

    # Sort and get top 2 jobs
    top_jobs = sorted(job_matches, key=lambda x: x[2], reverse=True)[:2]

    # If no matches, select 2 random jobs
    if not top_jobs:
        top_jobs = random.sample(list(df[["job_title", "job_summary", "extracted_skills"]].itertuples(index=False)), 2)
        top_jobs = [(clean_title(job.job_title), job.job_summary, 0, "N/A", job.extracted_skills) for job in top_jobs]

    # Extract degree (if matched)
    # selected_degree = top_jobs[0][3] if top_jobs[0][3] != "N/A" else selected_degree
    selected_degree=calculate_weight(user_skills,course_data)
    print(f'user skills: {user_skills}')
    print(f"selected degree: {selected_degree}")
    
    courses = get_courses(selected_degree, user_skills)
    print(courses)

    # Format response
    response = {
        "recommended_degree": selected_degree,
        "relevant_courses": [{"course_name": c[0], "hard_skills": list(set(c[1]["hard_skills"]))} for c in courses],
        "job_recommendations": [
            {"title": job[0], "summary": job[1], "required_skills": list({s.strip().lower() for s in job[4].split(',') if s.strip()})}
            for job in top_jobs
        ]
    }

    return jsonify(response)




@app.route('/degree_categories', methods=['GET'])
def get_degree_categories():
    unique_degrees = df["degree_category"].dropna().unique().tolist()  # Get unique non-null degree categories

    # Ensure the full list of degrees is included
    all_degrees = [
        "No Preference", "Digital Media", "Data Analyst", "Data Scientist",
        "Enterprise Systems", "Software Development", "Systems and Security"
    ]

    # Merge both lists, ensuring all expected degrees are included
    final_degrees = sorted(set(all_degrees + unique_degrees), key=lambda x: all_degrees.index(x) if x in all_degrees else float('inf'))

    return jsonify({"degree_categories": final_degrees})

top_skills_csv=pd.read_csv('merged_jobs_cleaned (6).csv')
all_jobs_df, skills_by_domain = load_job_data()

def get_courses_for_job_field(job_field):
    # Get skills for the given job field

    top_5_jobs = all_jobs_df[all_jobs_df['domain']==job_field].head(5)['Keyword'].tolist()

    for job in top_5_jobs:
        job_rows = top_skills_csv[top_skills_csv['job_title'].str.contains(re.escape(job), case=False, na=False)]

        # Count only within this job's descriptions
        skill_counts = {
            skill: job_rows['job_description'].str.contains(re.escape(skill), case=False, na=False).sum()
            for skill in skills_by_domain[job_field]
        }

        # top 5 most relevant skills for this job
        top_skills_for_job = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)[:5]   
    
    skills = [skill.lower() for skill, _ in top_skills_for_job]
    print(skills)
    # Prepare the courses with their skills
    courses_with_skills = []
    for course, course_info in course_data.items():
        hard_skills = course_info["hard_skills"]
        courses_with_skills.append({
            "course_name": course,
            "hard_skills": [skill.lower() for skill in hard_skills]
        })
    
    # Prepare the list to store matching courses and skills
    matching_courses_and_skills = []    
    for item in courses_with_skills:
        course_name = item['course_name']
        hard_skills = set(item['hard_skills'])  # Hard skills as a set
        matching_skills = list(set(hard_skills) & set(skills))



        
        if matching_skills:
            # Convert set to list before appending to the result
            matching_courses_and_skills.append({
                "course_name": course_name,
                "hard_skills": matching_skills  # List of matching skills
            })
    
    return matching_courses_and_skills

    
    





@app.route('/get_job_fields', methods=['GET'])
def get_job_fields():
    domain = all_jobs_df['domain'].unique().tolist()
    return jsonify(domain)

@app.route('/top_skills_per_field', methods=['POST'])
def top_skills_per_field():
    domain = request.json.get('job_field')

    if not domain:
        return jsonify({"error": "No job field selected"}), 400

    top_5_jobs = all_jobs_df[all_jobs_df['domain']==domain].head(5)['Keyword'].tolist()


    sunburst_data = []

    for job in top_5_jobs:
        job_rows = top_skills_csv[top_skills_csv['job_title'].str.contains(re.escape(job), case=False, na=False)]

        # Count only within this job's descriptions
        skill_counts = {
            skill: job_rows['job_description'].str.contains(re.escape(skill), case=False, na=False).sum()
            for skill in skills_by_domain[domain]
        }

        # top 5 most relevant skills for this job
        top_skills_for_job = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)[:5]

        for skill, count in top_skills_for_job:
            if count > 0:
                sunburst_data.append({
                    'Domain': domain,
                    'Job Title': job,
                    'Skill': skill,
                    'Count': count
                })

    # Convert to DataFrame
    sunburst_df = pd.DataFrame(sunburst_data)

    # Create sunburst: Domain to  Job Title to Skill
    fig = px.sunburst(
        sunburst_df,
        path=['Domain', 'Job Title', 'Skill'],
        values='Count',
        color='Job Title',
        title=f'{domain}: Top 5 Job Titles and Their Most Relevant Skills'
    )

    fig.update_traces(
        textinfo='label',
        textfont_size=12,
        insidetextorientation='radial',
        marker=dict(line=dict(color='white', width=2)),
        maxdepth=2
    )

    fig.update_layout(
        margin=dict(t=50, l=0, r=0, b=0),
        width=800, height=800,
        title_x=0.5,
        title_font_size=24
    )

    return jsonify(json.loads(fig.to_json()))

@app.route('/courses_for_field', methods=['POST'])
def courses_for_field():
    domain = request.json.get('job_field')

    if not domain:
        return jsonify({"error": "No job field selected"}), 400

    # Filter the data for the selected job field
    filtered_data = all_jobs_df[all_jobs_df['domain'] == domain]

    if filtered_data.empty:
        return jsonify({"error": "No data found for the selected job field"}), 404

    

    # Filter the courses JSON based on the selected job field and tech skills
    courses_for_field = get_courses_for_job_field(domain)

    return jsonify(courses_for_field)
    

# ========== Run Flask Server ========== #
if __name__ == '__main__':
    app.run(debug=True, port=5000)
