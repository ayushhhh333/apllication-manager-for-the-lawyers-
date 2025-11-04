from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Numeric
from datetime import date
from ..database import db, Base # Adjust import based on where 'db' is initialized

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id")) # Table name for Client model
    case_id = Column(Integer, ForeignKey("cases.id"), nullable=True)
    invoice_number = Column(String, unique=True, index=True)
    issue_date = Column(Date, default=date.today)
    due_date = Column(Date)
    total_amount = Column(Numeric(10, 2))
    status = Column(String, default="Pending")
    description = Column(Text, nullable=True)

    # Relationships
    client = db.relationship("Client", backref="invoices", lazy=True)
    case = db.relationship("Case", backref="invoices_for_case", lazy=True) # Use a different backref name if 'invoices' is already used by client
    payments = db.relationship("Payment", backref="invoice", lazy=True) # Assuming Payment model will have an invoice_id foreign key
