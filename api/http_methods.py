import requests

headers = {'Content-Type': 'application/json'}
cookie = ""


def method_get(url, params=None):
    if params is None:
        params = ""
    result = requests.get(url, params=params, headers=headers, cookies=cookie)
    return result
