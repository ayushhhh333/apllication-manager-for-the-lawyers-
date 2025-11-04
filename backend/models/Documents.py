from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from datetime import datetime
from ..database import db, Base # Adjust import based on where 'db' is initialized

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"))
    title = Column(String, index=True)
    file_name = Column(String)
    file_path = Column(String)
    upload_date = Column(DateTime, default=datetime.now)
    document_type = Column(String)
    description = Column(Text, nullable=True)

    # Relationship
    case = db.relationship("Case", backref="documents", lazy=True)
