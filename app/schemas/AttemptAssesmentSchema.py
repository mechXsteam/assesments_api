from pydantic import BaseModel


class AttemptAssessment(BaseModel):
    user_id: int
    assessment_name: str
