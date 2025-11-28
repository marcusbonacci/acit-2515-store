# Imports
import csv
from pathlib import Path
from sys import argv

try:
    from app import create_app
    from database import engine
    from models import Base
except ImportError as e:
    print("IMPORT ERROR", e)

# Functions
def create():
    print(f"Creating tables for {engine}")
    Base.metadata.create_all(engine)

def drop():
    print(f"Dropping tables for {engine}")
    Base.metadata.drop_all(engine)

def populate():
    print(f"Populating tables for {engine}")
    pass

# Main
if __name__ == "__main__":
    if len(argv) > 1:
        globals()[argv[1]]()
