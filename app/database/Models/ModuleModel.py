from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float

from app.database.base import Base


class ModuleModel(Base):
    __tablename__ = "module"

    id = Column(Integer, primary_key=True, autoincrement=True)
    assesment_id = Column(Integer, ForeignKey("assesments.id"), nullable=False)
    module_name = Column(String(150), nullable=False)
    module_time_duration = Column(Integer, nullable=False)
    module_description = Column(Text, nullable=False)
    module_category = Column(Integer, ForeignKey("module_category.id"), nullable=False)
    module_relevant_for = Column(String(255), nullable=False)
    module_sector = Column(String(150), nullable=False)
    module_difficulty = Column(String(255), nullable=False)

    category = relationship("ModuleCategoryModel", backref="module")

    @classmethod
    def get_marks_module_wise(cls):
        pass

    @classmethod
    def get_total_questions_module_wise(cls):
        pass



