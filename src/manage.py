# Imports
import csv
import warnings
from sys import argv
from sqlalchemy import select, func
import random
from datetime import datetime, timedelta

# Local Imports
try:
    from app import app
    from util import db
    from models import Customer, Product, Category, Order, ProductOrder
except ImportError as e:
    print("IMPORT ERROR", e)

# Variables

# Functions
def drop():
    print(f"Dropping all tables")
    db.drop_all()
    
def create():
    print(f"Creating all tables")
    db.create_all()

def populate():

    drop()
    create()

    print(f"Populating all tables")

    # Products
    with open("src/data/products.csv") as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            name, price, inventory, category = row
            ref_category = db.session.execute(
                select(Category)
                .where(Category.name == category)
            ).scalar()
            if (not ref_category): ref_category = Category(name = category)
            item = Product(
                name = name,
                price = price,
                inventory = inventory,
                category = ref_category
            )
            db.session.add(item)
        db.session.commit()

    with open("src/data/customers.csv") as file:
        data = csv.reader(file)
        next(data)
        for row in data:
            name, phone = row
            item = Customer(
                name = name,
                phone = phone
            )
            db.session.add(item)
        db.session.commit()

    for i in range(random.randint(30, 100)):
        create_random_order()

def create_random_order():
    # Construction
    customer = db.session.execute(select(Customer).order_by(func.random())).scalar()
    num_prods = random.randint(3, 6)
    products = db.session.execute(select(Product).order_by(func.random()).limit(num_prods)).scalars()

    rand_date = datetime.now() - timedelta(
        days=random.randint(1, 3),
        hours=random.randint(0, 15),
        minutes=random.randint(0, 30)
    )

    # Creation
    order = Order(customer=customer, created=rand_date)
    for product in products:
        newProduct = ProductOrder(
            product_id = product.id,
            order_id = order.id,
            quantity = random.randint(1, 7),
            product = product,
            order = order
        )
        db.session.add(newProduct)

    db.session.add(order)
    db.session.commit()

# Main
if __name__ == "__main__":
    if len(argv) > 1:
        try:
            with app.app_context():
                globals()[argv[1].lower()]()
        except Exception as e:
            warnings.warn(f"Function Error {e}")
