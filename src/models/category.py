# Imports
from sqlalchemy.orm import Mapped

# Local Imports
from database import db

# Model
class Category(db.Model):
    __tablename__ = "category"

    id: Mapped[int] = db.mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = db.mapped_column(db.String)
    products = db.relationship("Product", back_populates="category")