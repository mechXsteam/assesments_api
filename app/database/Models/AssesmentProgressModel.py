from sqlalchemy import Column, Integer, Boolean

from app.database.base import Base


# for tracking the candidate's progress on a particular assesment, if not completed then on which assesment he/she is
# currently on.

class AssessmentProgress(Base):
    __tablename__ = "assessment_progress"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # these two fields has to be updated whenever user submits and starts a new assesment
    assessment_id = Column(Integer, ForeignKey("assesments.id"), nullable=False)
    has_completed = Column(Boolean, default=False, nullable=True)

    # return the name of the assesment currently been attempted, else return attempted when user submits manually or
    # the time limit gets over
    @classmethod
    def get_candidate_assement_progress(cls):
        if not cls.has_completed:
            return cls.assessment_id
        return cls.has_completed
