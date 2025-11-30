# Imports
from flask import Blueprint, render_template
from sqlalchemy import select

# Local Imports
from models import Customer
from database import db

# Variables
customers_bp = Blueprint(
    "customers",
    __name__,
    static_folder="static",
    template_folder="templates"    
)

# Customer Route
@customers_bp.route("/")
def view_customers():
    statement = select(Customer)
    result = db.session.execute(statement).scalars()
    return render_template("customers.html", customers=result)