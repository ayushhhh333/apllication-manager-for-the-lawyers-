from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Numeric, Boolean
from datetime import datetime
from ..database import db, Base # Adjust import based on where 'db' is initialized

class TimeEntry(Base):
    __tablename__ = "time_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id")) # Table name for User model
    case_id = Column(Integer, ForeignKey("cases.id"))
    start_time = Column(DateTime, default=datetime.now)
    end_time = Column(DateTime)
    duration_minutes = Column(Integer)
    description = Column(Text)
    billable = Column(Boolean, default=True)
    rate_per_hour = Column(Numeric(10, 2), nullable=True)

    # Relationships
    user = db.relationship("User", backref="time_entries", lazy=True)
    case = db.relationship("Case", backref="time_entries", lazy=True)
    
