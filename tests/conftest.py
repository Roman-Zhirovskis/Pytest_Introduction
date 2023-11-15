import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register
from selenium import webdriver

from .factory import CategoryFactory, ProductFactory, UserFactory

register(UserFactory)
register(ProductFactory)
register(CategoryFactory)

# @pytest.fixture()
# def user_1(db):
#     print("Im in fixture")
#     user = User.objects.create_user("test-user")
#     print("create-user")
#     return user


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.fixture(
    params=[
        "chrome",
    ],
    scope="class",
)
def driver_init(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Chrome(
            executable_path=r"./chromedriver", options=options
        )
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Firefox(
            executable_path=r"./geckodriver", options=options
        )
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(
    params=["chrome1920", "chrome411"],
    scope="class",
)
def driver_init_screenshot(request):
    if request.param == "chrome1920":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        web_driver = webdriver.Chrome(
            executable_path=r"./chromedriver", options=options
        )
        request.cls.browser = "Chrome1920x1080"
    if request.param == "chrome411":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=411,823")
        web_driver = webdriver.Chrome(
            executable_path=r"./chromedriver", options=options
        )
        request.cls.browser = "Chrome411x823"

    request.cls.driver = web_driver
    yield
    web_driver.close()
