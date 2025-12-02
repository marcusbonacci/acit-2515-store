# Imports
from flask import Blueprint, render_template
from sqlalchemy import select

# Local Imports
from models import Category
from util import db

category_bp = Blueprint(
    "categories",
    __name__,
    static_folder="static",
    template_folder="templates"    
)

@category_bp.route("/")
def view_categories():
    statement = select(Category)
    result = db.session.execute(statement).scalars()
    return render_template("categories/index.html", categories=result)

@category_bp.route("/<string:name>")
def details(name):
    statement = select(Category).where(Category.name == name)
    result = db.session.execute(statement).scalar()
    if not result: return render_template("error.html", message="Resource not found", status_code=404), 404
    return render_template("categories/details.html", category=result.name, products=result.products)