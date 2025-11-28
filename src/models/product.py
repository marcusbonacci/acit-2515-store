from sqlalchemy import String, DECIMAL, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from . import Base

class Product(Base):
    __tablename__ = "product"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    price = mapped_column(DECIMAL(10, 2))
    inventory = mapped_column(Integer, default=0)
    category_id = mapped_column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

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