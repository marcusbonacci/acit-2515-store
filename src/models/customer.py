from sqlalchemy import String, DECIMAL, Integer
from sqlalchemy.orm import mapped_column

from .baseModel import Base

class Customer(Base):
    __tablename__ = "customer"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    phone = mapped_column(String)

    def __repr__(self):
        return f"<Customer {self.id}: {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
        }