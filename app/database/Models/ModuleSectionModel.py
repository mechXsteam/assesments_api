from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class SectionModel(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, autoincrement=True)
    section_name = Column(String(255), nullable=False)
    module_id = Column(Integer, ForeignKey("module.id"), nullable=False)
    module_duration = Column(Integer, nullable=False)
    score = Column(Integer, nullable=True)

    # Define the relationship with ModuleModel
    module = relationship("ModuleModel", backref="sections")

    def __repr__(self):
        return self.section_name

    @classmethod
    def calculate_marks_section_wise(cls):
        pass
