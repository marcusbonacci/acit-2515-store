# Imports
from sqlalchemy.orm import Mapped, relationship

# Local Imports
from database import db
class ProductOrder(db.Model):
    __tablename__ = "productorder"

    product_id = db.mapped_column(db.ForeignKey("product.id"), primary_key=True)
    order_id = db.mapped_column( db.ForeignKey("order.id"), primary_key=True)
    quantity = db.mapped_column(db.Integer, nullable=False)

    product = db.relationship("Product")
    order = db.relationship("Order", back_populates="items")

    def __repr__(self):
        return f"<ProductOrder {self.product_id}: {self.order_id}>"

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "order_id": self.order_id,
            "quantity": self.quantity,
            "product": self.product,
            "order": self.order
        }