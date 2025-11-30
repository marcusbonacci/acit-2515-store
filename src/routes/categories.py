# Imports
from flask import Blueprint, render_template
from sqlalchemy import select

# Local Imports
from models import Category
from database import db

categories_bp = Blueprint(
    "categories",
    __name__,
    static_folder="static",
    template_folder="templates"    
)

@categories_bp.route("/")
def view_categories():
    statement = select(Category)
    result = db.session.execute(statement).scalars()
    return render_template("categories.html", categories=result)

@categories_bp.route("/<string:name>")
def details(name):
    print("AAAAAAAAAAAAAAAAAAAAAAAAA", name)
    statement = select(Category).where(Category.name == name)
    result = db.session.execute(statement).scalar()
    return render_template("category_details.html", category=result.name, products=result.products)

