import time
from config import settings

from api.http_methods import method_get
from page_object.login_page import PageLogin


def test_login_wrong_user_name(browser_fixture):
    url = method_get(settings.url_with_users).json()
    PageLogin(browser_fixture).login_wrong_user_name(url[0]["name"])


def test_wrong_phone(browser_fixture):
    url = method_get(settings.url_with_users).json()
    PageLogin(browser_fixture).wrong_phone(url[0]["phone"])


def test_empty_field_login(browser_fixture):
    PageLogin(browser_fixture).empty_field_login()


def test_empty_field_phone(browser_fixture):
    PageLogin(browser_fixture).empty_field_phone()
    time.sleep(5)


def test_user_does_not_exist(browser_fixture):
    url = method_get(settings.url_with_users).json()
    name_1 = url[0]["name"].replace(" ", "")
    result_name = name_1 + url[1]["name"].replace(" ", "")
    PageLogin(browser_fixture).user_does_not_exist(result_name)
