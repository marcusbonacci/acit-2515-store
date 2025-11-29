# Imports
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

# Local Imports
from . import Base

# Model
class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    products = relationship("Product", back_populates="category")