# Imports
from sqlalchemy.orm import Mapped

# Local Import
from database import db

# Model
class Product(db.Model):
    __tablename__ = "product"

    id: Mapped[int] = db.mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = db.mapped_column(db.String)
    price: Mapped[float] = db.mapped_column(db.DECIMAL(10, 2))
    inventory: Mapped[int] = db.mapped_column(db.Integer, default=0)
    category_id: Mapped[int] = db.mapped_column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product {self.id}: {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "inventory": self.inventory,
            "category": self.category,
        }