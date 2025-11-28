# Imports
import csv
import warnings
from pathlib import Path
from sys import argv

from sqlalchemy import select

try:
    from database import Session, engine
    from models import Base, Customer, Product, Category
except ImportError as e:
    print("IMPORT ERROR", e)

# Variables
data_files = [
    "products.csv",
    "customers.csv"
]

session = Session()

# Functions
def create():
    print(f"Creating tables for {engine}")
    Base.metadata.create_all(engine)


def drop():
    print(f"Dropping tables for {engine}")
    Base.metadata.drop_all(engine)

def populate():

    drop()
    create()

    print(f"Populating tables for {engine}")
    for file in data_files:
        try:
            file_path = Path(__file__).parent.parent / file
            file_name = str.removesuffix(file, "s.csv")
            if (not file_path): raise(f"Couldn't resolve file: {file}")

            with open(file_path) as file:
                data = csv.DictReader(file)
                for row in data:
                    item = globals()[file_name.capitalize()](**row)
                    session.add(item)

                print(f"Commiting {file_name} to database")
                session.commit()

        except Exception as e:
            warnings.warn(f"manage-db.py: {e}")


# Main
if __name__ == "__main__":
    if len(argv) > 1:
        globals()[argv[1]]()
