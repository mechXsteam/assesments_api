from app.schemas.AttemptAssesmentSchema import AttemptAssessment


@app.post("/attempt-assessment/")
async def attempt_assessment(attempt: AttemptAssessment):
    # Assuming you have SQLAlchemy models defined

    user = db.query(User).filter(User.id == attempt.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    assessment = Assessment(
        job_opening_id=1,  # Replace with actual job opening ID
        assessment_name=attempt.assessment_name,
        user_id=user.id
    )

    db.add(assessment)
    db.commit()
    db.refresh(assessment)
    db.close()
    return {"message": "Assessment attempted successfully"}


@app.post("/submit-response/")
async def submit_response(response: UserResponseInput):
    # Assuming you have SQLAlchemy models defined

    user_response = UserResponse(
        user_id=response.user_id,
        question_id=response.question_id,
        response=response.response
    )

    db.add(user_response)
    db.commit()
    db.refresh(user_response)
    db.close()
    return {"message": "Response submitted successfully"}
