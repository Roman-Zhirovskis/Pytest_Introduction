import pytest
from django.test import LiveServerTestCase
from selenium import webdriver

# class TestBrowserChrome(LiveServerTestCase):
#     def test_example(self):
#         driver = webdriver.Chrome("./chromedriver")
#         driver.get(("%s%s" % (self.live_server_url, "/admin")))
#         assert "Log in | Django site admin" in driver.title


# class TestBrowserFirefox(LiveServerTestCase):
#     def test_example(self):
#         driver = webdriver.Firefox(executable_path="./geckodriver")
#         driver.get(("%s%s" % (self.live_server_url, "/admin")))
#         assert "Log in | Django site admin" in driver.title


# Example2 run test in headless mode
# class TestBrowser2(LiveServerTestCase):
#     def test_example(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Chrome(executable_path=r"./chromedriver", options=options)
#         driver.get(("%s%s" % (self.live_server_url, "/admin")))
#         assert "Log in | Django site admin" in driver.title


# Example 3 (fixture)


# @pytest.mark.usefixtures("chrome_driver_init")
# class Test_Url_Chrome(LiveServerTestCase):
#     def test_open_url(self):
#         self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in self.driver.title


# Example 4 (not working yet)
# @pytest.mark.usefixtures("chrome_driver_init")
# class Test_Url_Chrome1(LiveServerTestCase):
#     def test_open_url(self, live_server):
#         self.driver.get(("%s%s" % (self.live_server.url, "/admin/")))
#         assert "Log in | Django site admin" in self.driver.title


# Example 5 Trying run firefox browser (FireFox openning error)
# class TestBrowser2(LiveServerTestCase):
#     def test_example(self):
#         options = webdriver.FirefoxOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Firefox(executable_path=r"./geckodriver", options=options)
#         driver.get(("%s%s" % (self.live_server_url, "/admin")))
#         assert "Log in | Django site admin" in driver.title


# Example 5(Work onli in chromedriver choise)
# @pytest.mark.usefixtures("driver_init")
# class Test_URL_Chrome:
#     def test_open_url(self, live_server):
#         self.driver.get(("%s%s" % (live_server.url, "/admin/")))
#         assert "Log in | Django site admin" in self.driver.title
