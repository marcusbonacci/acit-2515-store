from database import Session, engine
from models import Product, Customer, Base


def create_app():
    print("Hello from store!")

    # print(engine)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    product = Product(name="eggs", price=12.34, inventory=10)
    session = Session()
    session.add(product)
    session.commit()

    # print("#"*12)
    # print(repr(product))
    # print(product.to_dict())


if __name__ == "__main__":
    main()
