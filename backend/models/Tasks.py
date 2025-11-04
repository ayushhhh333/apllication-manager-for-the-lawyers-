from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from datetime import date
from ..database import db, Base # Adjust import based on where 'db' is initialized

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"))
    assigned_to_id = Column(Integer, ForeignKey("users.id")) # Table name for User model
    title = Column(String, index=True)
    description = Column(Text)
    due_date = Column(Date)
    status = Column(String, default="Pending")
    priority = Column(String, default="Medium")

    # Relationships
    case = db.relationship("Case", backref="tasks", lazy=True)
    assigned_to_user = db.relationship("User", backref="tasks", lazy=True) # Class name for User model
