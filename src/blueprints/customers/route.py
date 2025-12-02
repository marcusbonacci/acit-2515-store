# Imports
from flask import Blueprint, render_template
from sqlalchemy import select

# Local Imports
from models import Customer
from util import db

# Variables
customer_bp = Blueprint(
    "customers",
    __name__,
    static_folder="static",
    template_folder="templates"    
)

# Customer Route
@customer_bp.route("/")
def view_customers():
    statement = select(Customer)
    result = db.session.execute(statement).scalars()
    return render_template("customers/index.html", customers=result)

@customer_bp.route("/<int:id>")
def details(id):
    statement = select(Customer).where(Customer.id == id)
    result = db.session.execute(statement).scalar()
    if not result: return render_template("error.html", message="Resource not found", status_code=404), 404
    return render_template("customers/details.html", customer=result)

