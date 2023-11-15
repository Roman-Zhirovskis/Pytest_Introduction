import pytest

# from django.contrib.auth.models import User


# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user("test-user")


# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     print("Im in test_case")
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") is True


# def test_new_user(user_factory):
#     print(user_factory.username)
#     assert True


# @pytest.mark.django_db
# def test_new_user(user_factory):
#     user = user_factory.create()
#     print(user.username)
#     print(user.is_staff)
#     assert True


def test_product(product_factory):
    product = product_factory.build()
    print(product.description)
    assert True


@pytest.mark.django_db
def test_product2(product_factory):
    product = product_factory.create()
    print(product.description)
    assert True
