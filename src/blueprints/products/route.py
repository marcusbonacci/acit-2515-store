# Imports
from flask import Blueprint, render_template
from sqlalchemy import select

# Local Imports
from models import Product
from database import db

product_bp = Blueprint(
    "products",
    __name__,
    static_folder="static",
    template_folder="templates"    
)

@product_bp.route("/")
def view_products():
    statement = select(Product)
    result = db.session.execute(statement).scalars()
    return render_template("products/index.html", products=result)

@product_bp.route("/<int:id>")
def details(id):
    statement = select(Product).where(Product.id == id )
    result = db.session.execute(statement).scalar()
    if not result: return render_template("error.html", message="Resource not found", status_code=404), 404
    return render_template("products/details.html", product=result)