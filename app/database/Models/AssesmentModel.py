from sqlalchemy import Column, Integer, String, Text, ForeignKey

from app.database.base import Base


# for creating an assesment by the recruiter

class AssesmentModel(Base):
    __tablename__ = "assesments"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # each assesment will be associated with a job_opening in many to one fashion
    job_opening_id = Column(Integer, ForeignKey("job_opening.id"))

    name = Column(String(150), unique=True, nullable=False)
    job_role = Column(String(150), nullable=False)
    sector = Column(String(150), nullable=False)
    instructions = Column(Text, nullable=False)
    passing_percentage = Column(Integer, nullable=False, default=33)

    @classmethod
    def create_assesment(cls, db, **kwargs):
        assesment = AssesmentModel(**kwargs)
        db.add(assesment)
        db.commit()
        db.refresh()

    @classmethod
    def get_assesment_by_id(cls, db, assesment_id: int):
        assesment = db.query(cls).get(assesment_id)
        return assesment

    # returns all the candidates who attempted a particular assesments
    @classmethod
    def get_candidate_attempted_assessment(cls, db):
        pass

    # returns all the candidates who didn't complete a particular assesments
    @classmethod
    def get_candidate_not_completed_assessment(cls, db):
        pass

    # returns all the candidates who passed a particular assesments
    @classmethod
    def get_candidate_passed_assessment(cls, db):
        pass

    # returns all the candidates who failed a particular assesments
    @classmethod
    def get_candidate_failed_assessment(cls, db):
        pass

    # returns the proctoring passed candidates
    @classmethod
    def get_candidate_proctoring_passed(cls, db):
        pass

    # returns the proctoring failed candidates
    @classmethod
    def get_candidate_proctoring_failed(cls, db):
        pass

    @classmethod
    def calculate_marks_section_wise(cls):
        pass

    @classmethod
    def get_candidate_status(cls):
        pass

    def __repr__(self):
        return f"assesment_name:{self.name}"
