# Imports
from pathlib import Path
from sqlalchemy import select
from flask import Flask, render_template

# Local Imports
from util import db
from blueprints import category_bp, customer_bp, product_bp, order_bp

from models import Order

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
            return render_template("index.html")
        
        # Register Blueprints
        app.register_blueprint(customer_bp, url_prefix="/customers")
        app.register_blueprint(product_bp, url_prefix="/products")
        app.register_blueprint(category_bp, url_prefix="/categories")
        app.register_blueprint(order_bp, url_prefix="/orders")

        # my_order = db.session.execute(select(Order)).scalar()
        # # print(my_order.items)
        # my_order.complete()

    app.run(debug=True, port=8888)

if __name__ == "__main__":
    create_app()
