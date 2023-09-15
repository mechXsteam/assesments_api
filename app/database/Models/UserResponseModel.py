from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class UserResponseModel(Base):
    __tablename__ = "user_responses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    response = Column(String(255), nullable=False)

    # Define the relationship with QuestionModel
    question = relationship("QuestionModel", backref="user_responses")

    def __repr__(self):
        return self.response
