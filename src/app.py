# Imports
from pathlib import Path
from sqlalchemy import select
from flask import Flask, render_template

# Local Imports
from database import db
from models import Product, Customer, Category

# Variables

# Functions
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.instance_path = Path(__file__).resolve().parent / "data"
db.init_app(app)

def create_app():
    with app.app_context():
        @app.route("/")
        def home():
            return render_template("home.html")
        
        @app.route("/products")
        def products():
            statement = select(Product)
            products = db.session.execute(statement).scalars()
            return render_template("products.html", products=products)

        @app.route("/customers")
        def customers():
            statement = select(Customer)
            customers = db.session.execute(statement).scalars()
            return render_template("customers.html", customers=customers)

        @app.route("/categories")
        def categories():
            statement = select(Category)
            category = db.session.execute(statement).scalars()
            return render_template("categories.html", categories=category)


    app.run(debug=True, port=8888)

if __name__ == "__main__":
    create_app()
