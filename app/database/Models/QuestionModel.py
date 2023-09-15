from sqlalchemy import Column, Integer, String, Text, ForeignKey

from app.database.base import Base


class QuestionModel(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    module_id = Column(Integer, ForeignKey('module.id'))
    question_text = Column(String(500), nullable=False)
    question_options = Column(Text, nullable=False)
    correct_answer = Column(String(500), nullable=False)
    question_level = Column(String(150), nullable=False)
    question_subjects = Column(String(255), nullable=False)
    question_topics = Column(String(255), nullable=False)

    module = relationship("ModuleModel", backref="questions")

    def __repr__(self):
        return self.question_text
