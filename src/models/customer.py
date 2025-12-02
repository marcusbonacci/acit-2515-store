from database import db

class Customer(db.Model):
    __tablename__ = "customer"

    id = db.mapped_column(db.Integer, primary_key=True)
    name = db.mapped_column(db.String)
    phone = db.mapped_column(db.String)
    orders = db.relationship("Order", back_populates="customer")

    def __repr__(self):
        return f"<Customer {self.id}: {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "orders": self.orders
        }