# Imports
from sqlalchemy.orm import Mapped
from datetime import datetime

# Local Imports
from database import db

class Order(db.Model):
    __tablename__ = "order"

    id = db.mapped_column(db.Integer, primary_key=True)
    items = db.relationship("ProductOrder", back_populates="order")
    customer_id = db.mapped_column(db.Integer, db.ForeignKey("customer.id"))
    customer = db.relationship("Customer")
    
    created = db.mapped_column(db.DateTime, nullable=False, default=db.func.now())
    completed = db.mapped_column(db.DateTime, default=None)
    amount = db.mapped_column(db.DECIMAL(6, 2), default=None)

    def estimate(self) -> float:
        total = 0
        for item in self.items:
            total += (item.quantity * item.product.price)
        return total

    def complete(self) -> bool:
        for item in self.items:
            if (item.product.inventory >= item.quantity):
                item.product.inventory -= item.quantity
            else:
                raise ValueError("Not enough items to complete order")
        self.amount = self.estimate()
        self.completed = db.func.now()

        db.session.commit()
        return True


    def __repr__(self):
        return f"<Order {self.id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "items": self.items,
            "customer_id": self.customer_id,
            "customer": self.customer,
            "created": self.created,
            "amount": self.amount
        }