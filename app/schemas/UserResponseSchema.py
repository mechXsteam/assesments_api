from pydantic import BaseModel


class UserResponseInput(BaseModel):
    user_id: int
    question_id: int
    response: str
