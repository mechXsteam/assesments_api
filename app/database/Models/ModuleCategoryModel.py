from sqlalchemy import Column, Integer, String, Boolean

from app.database.base import Base


class ModuleCategoryModel(Base):
    __tablename__ = "module_category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_mcq = Column(Boolean, nullable=True)  # mcq type assesment
    is_free_text = Column(Boolean, nullable=True)  # free text type assesment

