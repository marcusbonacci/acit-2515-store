# Imports
import csv
import warnings
from sys import argv
from sqlalchemy import select

# Local Imports
try:
    from app import app
    from database import db
    from models import Customer, Product, Category
except ImportError as e:
    print("IMPORT ERROR", e)

# Variables

# Functions
def drop():
    print(f"Dropping tables for {db.engine}")
    db.drop_all(db.engine)
    
def create():
    print(f"Creating tables for {db.engine}")
    db.create_all(db.engine)


def populate():

    drop()
    create()

    print(f"Populating tables for {db.engine}")

    # Products
    with open("products.csv") as file:
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

    with open("customers.csv") as file:
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

# Main
if __name__ == "__main__":
    if len(argv) > 1:
        try:
            with app.app_context():
                globals()[argv[1].lower()]()
        except Exception as e:
            warnings.warn(f"Function Error {e}")
