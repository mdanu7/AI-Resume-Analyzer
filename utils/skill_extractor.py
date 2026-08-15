SKILLS = [
    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "kotlin",

    # Data Science / AI
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "natural language processing",
    "nlp",
    "computer vision",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "keras",

    # Data
    "sql",
    "mysql",
    "postgresql",
    "pandas",
    "numpy",
    "excel",
    "power bi",
    "tableau",
    "statistics",

    # Web
    "html",
    "css",
    "react",
    "node.js",
    "django",
    "flask",
    "bootstrap",
    "rest api",

    # Cloud / DevOps
    "aws",
    "azure",
    "docker",
    "kubernetes",
    "jenkins",
    "linux",
    "git",

    # Cybersecurity
    "cybersecurity",
    "networking",
    "firewalls",
    "cryptography",
    "siem",

    # Testing
    "selenium",
    "software testing",
    "automation testing",

    # Design
    "figma",
    "ui design",
    "ux design",
    "wireframing",
    "prototyping"
]

def extract_skills(resume_text):
    """
    Extract skills from resume text.
    """

    resume_text = resume_text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills
