# Imports
from pathlib import Path
from sqlalchemy import select
from flask import Flask, render_template

# Local Imports
from database import db
from models import Product, Customer, Category
from routes import customers_bp, products_bp, categories_bp

# Blueprints

# Variables

# Functions
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev",
    SQLALCHEMY_DATABASE_URI="sqlite:///data.db"
)
app.instance_path = Path(__file__).resolve().parent / "data"
db.init_app(app)

def create_app():
    with app.app_context():

        @app.route("/")
        def home():
            return render_template("home.html")
        
        # Register Blueprints
        app.register_blueprint(customers_bp, url_prefix="/customers")
        app.register_blueprint(products_bp, url_prefix="/products")
        app.register_blueprint(categories_bp, url_prefix="/categories")

    app.run(debug=True, port=8888)

if __name__ == "__main__":
    create_app()
