from config import settings
from utils.utils import write_to_file


class PageLogin:
    placeholder_login = "Логин или email"
    error_text = ".Textinput-Hint"

    def __init__(self, browser_fixture):
        self.browser_fixture = browser_fixture

    def login_wrong_user_data(self, data):
        page = self.browser_fixture
        page.goto(settings.url_test_env)
        page = self.browser_fixture
        page.goto(settings.url_test_env)
        page.get_by_placeholder(self.placeholder_login).click()
        page.get_by_placeholder(self.placeholder_login).fill(data)
        page.get_by_placeholder(self.placeholder_login).press("Enter")
        error_elem = page.locator(self.error_text)
        text = error_elem.text_content()
        print(text)
        if text == "Такой логин не подойдет":
            write_to_file("Тест прошёл")
        else:
            write_to_file("Тест не прошёл")
