# Imports
from flask import Blueprint, render_template
from sqlalchemy import select

# Local Imports
from models import Product
from database import db

products_bp = Blueprint(
    "products",
    __name__,
    static_folder="static",
    template_folder="templates"    
)

@products_bp.route("/")
def view_products():
    statement = select(Product)
    result = db.session.execute(statement).scalars()
    return render_template("products.html", products=result)