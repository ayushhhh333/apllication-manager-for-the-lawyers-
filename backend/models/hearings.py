from sqlalchemy import Column, Integer, DateTime, String, Text, ForeignKey
from ..database import db, Base 
class Hearing(Base):
    __tablename__ = "hearings"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"))
    hearing_date = Column(DateTime)
    court = Column(String)
    judge = Column(String)
    details = Column(Text)
    next_hearing_date = Column(DateTime, nullable=True)

    case = db.relationship("Case", backref="hearings", lazy=True)
