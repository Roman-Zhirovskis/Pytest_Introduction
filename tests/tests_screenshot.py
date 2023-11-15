import os
import time

import pytest
from django.test import LiveServerTestCase
from selenium import webdriver


def take_screenshot(driver, name):
    time.sleep(0.5)
    abstract_path_dir = os.path.dirname(__file__), "screenshot", os.path.dirname(name)

    os.makedirs(
        os.path.join(*abstract_path_dir),
        exist_ok=True,
    )
    driver.save_screenshot(os.path.join(os.path.dirname(__file__), "screenshot", name))


def test_example(live_server):
    driver = webdriver.Chrome("./chromedriver")
    driver.get(("%s%s" % (live_server.url, "/admin")))
    take_screenshot(driver=driver, name="screenshot/admin.png")


@pytest.mark.usefixtures("driver_init_screenshot")
class Screenshot:
    def screenshot_admin(self, live_server):
        self.driver.get(("%s%s" % (live_server.url, "/admin/")))
        take_screenshot(self.driver, "admin/" + "admin" + self.browser + ".png")
        assert "Log in | Django site admin" in self.driver.title
