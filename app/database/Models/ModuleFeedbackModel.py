from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.database.base import Base


class ModuleFeedbackModel(Base):
    __tablename__ = "module_feedback"

    id = Column(Integer, primary_key=True, autoincrement=True)
    module_feedback = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    module_id = Column(Integer, ForeignKey('module.id'), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())
