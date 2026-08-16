import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load job dataset
jobs = pd.read_csv("dataset/jobs.csv")

# Combine skills and description
jobs["job_text"] = (
    jobs["required_skills"] + " " + jobs["description"]
)

# Create TF-IDF model
vectorizer = TfidfVectorizer(
    stop_words="english"
)

# Convert jobs into vectors
job_vectors = vectorizer.fit_transform(
    jobs["job_text"]
)


def recommend_jobs(resume_text, top_n=5):

    # Convert resume into TF-IDF vector
    resume_vector = vectorizer.transform(
        [resume_text]
    )

    # Calculate similarity
    similarity_scores = cosine_similarity(
        resume_vector,
        job_vectors
    ).flatten()

    # Copy jobs
    jobs_copy = jobs.copy()

    # Add percentage score
    jobs_copy["match_score"] = (
        similarity_scores * 100
    )

    # Sort highest to lowest
    jobs_copy = jobs_copy.sort_values(
        by="match_score",
        ascending=False
    )

    # Return top jobs
    return jobs_copy.head(top_n)[
        [
            "job_title",
            "required_skills",
            "match_score"
        ]
    ]

def calculate_skill_gap(resume_skills, required_skills):

    # Convert resume skills to lowercase
    resume_skill_set = set(
        skill.lower().strip()
        for skill in resume_skills
    )

    # Convert required skills into a list
    required_skill_list = [
        skill.lower().strip()
        for skill in required_skills.split(",")
    ]

    matching_skills = []
    missing_skills = []

    for skill in required_skill_list:

        if skill in resume_skill_set:
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matching_skills, missing_skills