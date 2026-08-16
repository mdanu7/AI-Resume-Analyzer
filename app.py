from flask import Flask, render_template, request
import os

from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.job_recommender import (
    recommend_jobs,
    calculate_skill_gap
)
from utils.resume_scorer import calculate_resume_score

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return "No resume uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "No file selected"

    if not file.filename.lower().endswith(".pdf"):
        return "Please upload a PDF file"

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(file_path)

    resume_text = extract_text_from_pdf(file_path)

    skills = extract_skills(resume_text)

    recommendations = recommend_jobs(resume_text)

    best_job = recommendations.iloc[0]

    matching_skills, missing_skills = calculate_skill_gap(
        skills,
        best_job["required_skills"]
    )

    resume_score = calculate_resume_score(
    resume_text,
    skills,
    recommendations
)

    return render_template(
        "result.html",
        skills=skills,
        resume_text=resume_text,
        recommendations=recommendations.to_dict("records"),
        matching_skills=matching_skills,
        missing_skills=missing_skills,
        resume_score=resume_score
    )


if __name__ == "__main__":
    app.run(debug=True)