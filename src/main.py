# Imports
from sqlalchemy import select

# Local Imports
from database import Session
from models import Product, Customer, Base

# Variables
session = Session()

# Functions
def main():
    print("Hello from store!")

    statement = select(Product)
    results = session.execute(statement)
    for item in results.scalars():
        print(item.name)

# Main
if __name__ == "__main__":
    main()
