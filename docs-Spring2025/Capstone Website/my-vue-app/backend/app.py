from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin  # ✅ Import CORS
import plotly.express as px
import pandas as pd
import json
import re
import random
from collections import Counter

app = Flask(__name__)
CORS(app)  

# ========== Load Data Once (Global Variables) ========== #
combined_df = pd.read_json('combined_df.json', orient='records')
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
    return render_template('index.html')

@app.route('/sunburst')
def sunburst_chart():
    fig = px.sunburst(
        combined_df,
        path=['Domain', 'Category', 'Keyword'],
        values='Count',
        title='Job Market Overview: Click to Explore Technical & Soft Skills',
        color='Domain',
        color_discrete_sequence=px.colors.qualitative.Pastel,
        branchvalues='total'
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

# ========== Chatbot API Routes ========== #

# Function to clean job titles
def clean_title(title):
    return re.split(r"[-(]", title, 1)[0].strip()

# Function to get relevant courses
def get_courses(degree_category, user_skills):

    courses = list(course_data.get(degree_category, {}).items())  # Get courses for the degree
    categorized_courses = {"1000": [], "2000": [], "3000": [], "4000": []}
    matched_courses = []

    for course_name, attributes in courses:
        match = re.search(r"(\d{4})", course_name)
        if match:
            level = match.group(1)[0] + "000"
            if level in categorized_courses:
                categorized_courses[level].append((course_name, attributes))

        # Convert course skills to lowercase and remove spaces
        course_skills = {skill.strip().lower() for skill in attributes["hard_skills"]}

        # Fix skill matching logic
        if any(skill in course_skills for skill in user_skills):
            matched_courses.append((course_name, attributes))

    # Debugging: Print Matched Courses
    print(f"Matched Courses: {matched_courses}")

    # If no exact matches, return 1 random course per level
    selected_courses = []
    for level in ["1000", "2000", "3000", "4000"]:
        if categorized_courses[level]:
            selected_courses.append(random.choice(categorized_courses[level]))

    # Ensure we always return at least 3 courses
    if not matched_courses and selected_courses:
        matched_courses = selected_courses[:3]

    # Debugging: Print Final Selected Courses
    print(f"Final Selected Courses: {matched_courses}")

    return matched_courses[:3]


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
    selected_degree = top_jobs[0][3] if top_jobs[0][3] != "N/A" else selected_degree
    courses = get_courses(selected_degree, user_skills)

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


@app.route('/top_skills', methods=['GET'])
def get_top_skills():
    return jsonify({"top_skills": random.sample(top_100_skills, 10)})

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

top_skills_csv=pd.read_csv('top_10_jobs_per_field (4).csv')
@app.route('/get_job_fields', methods=['GET'])

def get_job_fields():
    job_fields = top_skills_csv['job_field'].unique().tolist()
    return jsonify(job_fields)

@app.route('/top_skills_per_field', methods=['POST'])
def top_skills_per_field():
    job_field = request.json.get('job_field')
    
    if not job_field:
        return jsonify({"error": "No job field selected"}), 400

    # Filter the data for the selected job field
    filtered_data = top_skills_csv[top_skills_csv['job_field'] == job_field]
    
    # Debugging: Print the filtered data
    print(f"Filtered Data for {job_field}: {filtered_data}")

    # If no data matches, return an error
    if filtered_data.empty:
        return jsonify({"error": f"No skills found for job field: {job_field}"}), 404

    # Create a dictionary to store skills for each job title
    job_title_skills = {}

    # Iterate through the filtered data
    for _, row in filtered_data.iterrows():
        job_title = row['Top Job Title']
        skills = row['Top Skill']

        # If this job title is not already in the dictionary, initialize it with an empty set
        if job_title not in job_title_skills:
            job_title_skills[job_title] = set()

        # Add the skill to the set (automatically avoids duplicates)
        job_title_skills[job_title].add(skills)

    # Convert the dictionary to a list of job titles and their associated unique skills
    result = [{"job_title": job_title, "skills": list(skills)} for job_title, skills in job_title_skills.items()]

    # Debugging: Check the result being returned
    print(f"Job Titles and Skills: {result}")

    return jsonify(result)


    

# ========== Run Flask Server ========== #
if __name__ == '__main__':
    app.run(debug=True, port=5000)
