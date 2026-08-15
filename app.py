from flask import Flask, render_template, request
import os

from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Check whether a file was uploaded
    if "resume" not in request.files:
        return "No resume uploaded"

    file = request.files["resume"]

    # Check filename
    if file.filename == "":
        return "No file selected"

    # Only allow PDF
    if not file.filename.lower().endswith(".pdf"):
        return "Please upload a PDF file"

    # Save uploaded PDF
    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(file_path)

    # Extract text from PDF
    resume_text = extract_text_from_pdf(file_path)

    # Extract skills
    skills = extract_skills(resume_text)

    return render_template(
        "result.html",
        skills=skills,
        resume_text=resume_text
    )


if __name__ == "__main__":
    app.run(debug=True)