# # Imports
# import pytest

# # Local Imports
# from src.models import Product, Category

# @pytest.fixture
# def test_category():
#     return Category(
#         id = 1,
#         name = "Produce"
#     )

# @pytest.fixture
# def test_apple():
#     return Product(
#         id = 1,
#         name = "Apple",
#         price = 1.25,
#         category_id = 1,
#         category = test_category()
#     )

# def test_product(test_apple):
#     product = test_apple()
#     print(product)