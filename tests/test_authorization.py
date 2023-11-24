import time

from api import http_methods
from config import settings
from playwright.sync_api import expect
from page_object.login_page import PageLogin


def test_01(browser_fixture):
    url = http_methods.method_get(settings.url_with_users).json()
    PageLogin(browser_fixture).login_wrong_user_data(url[0]["name"])

    time.sleep(2)
