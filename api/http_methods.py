import allure
import requests

"""List HTTP methods"""

headers = {'Content-Type': 'application/json'}
cookie = ""


def method_get(url, params=None):
    with allure.step("GET"):
        if params is None:
            params = ""
        result = requests.get(url, params=params, headers=headers, cookies=cookie)
        return result
