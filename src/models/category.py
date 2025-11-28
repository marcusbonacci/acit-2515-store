# Imports
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, relationship

# Local Imports
from . import Base

# Classes
class Category(Base):
    __tablename__ = "categories"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    products = relationship("Product", back_populates="category")