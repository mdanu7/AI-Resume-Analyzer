def calculate_resume_score(
    resume_text,
    detected_skills,
    recommendations
):

    # --------------------------------
    # 1. SKILLS SCORE - 50%
    # --------------------------------

    skill_score = min(
        len(detected_skills) * 5,
        50
    )


    # --------------------------------
    # 2. CONTENT SCORE - 20%
    # --------------------------------

    text_length = len(resume_text.split())

    if text_length >= 400:

        content_score = 20

    elif text_length >= 250:

        content_score = 15

    elif text_length >= 100:

        content_score = 10

    else:

        content_score = 5


    # --------------------------------
    # 3. JOB MATCH SCORE - 30%
    # --------------------------------

    if recommendations is not None and len(recommendations) > 0:

        # recommendations is a Pandas DataFrame
        best_match = recommendations.iloc[0]["match_score"]

        job_score = best_match * 0.30

    else:

        job_score = 0


    # --------------------------------
    # FINAL SCORE
    # --------------------------------

    final_score = (
        skill_score
        + content_score
        + job_score
    )


    # Keep score between 0 and 100

    final_score = min(
        round(final_score),
        100
    )


    return final_score