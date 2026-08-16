def calculate_resume_score(
    resume_text,
    detected_skills,
    recommendations
):

    score = 0

    # -------------------------
    # 1. Skills Score: 40 points
    # -------------------------

    skill_score = min(
        len(detected_skills) * 5,
        40
    )

    score += skill_score


    # -------------------------
    # 2. Resume Content: 20 points
    # -------------------------

    word_count = len(resume_text.split())

    if word_count >= 300:
        content_score = 20

    elif word_count >= 200:
        content_score = 15

    elif word_count >= 100:
        content_score = 10

    else:
        content_score = 5

    score += content_score


    # -------------------------
    # 3. Job Compatibility: 40 points
    # -------------------------

    if len(recommendations) > 0:

        best_match = recommendations.iloc[0]["match_score"]

        compatibility_score = min(
            best_match * 0.4,
            40
        )

    else:

        compatibility_score = 0


    score += compatibility_score


    return round(score, 2)