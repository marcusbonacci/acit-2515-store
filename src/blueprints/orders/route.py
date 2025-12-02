# Imports
from flask import Blueprint, render_template, redirect, url_for
from sqlalchemy import select

# Local Imports
from models import Order
from database import db

# Variables
order_bp = Blueprint(
    "orders",
    __name__,
    static_folder="static",
    template_folder="templates"    
)

# Customer Route
@order_bp.route("/")
def view_orders():
    statement = select(Order)
    result = db.session.execute(statement).scalars()
    return render_template("orders/index.html", orders=result)

@order_bp.route("/<int:id>")
def details(id):
    statement = select(Order).where(Order.id == id)
    result = db.session.execute(statement).scalar()
    if not result: return render_template("error.html", message="Resource not found", status_code=404), 404
    return render_template("orders/details.html", order=result)

@order_bp.route("/<int:id>/complete", methods=["POST"])
def complete(id):
    statement = select(Order).where(Order.id == id)
    result = db.session.execute(statement).scalar()
    if not result: return render_template("error.html", message="Resource not found", status_code=404), 404
    try:
        result.complete()
    except ValueError as e:
        return render_template("error.html", message=f"{e}", status_code=400), 400
    
    return redirect(url_for('orders.details', id=result.id))

