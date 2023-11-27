from config import settings
from utils.helpers import write_to_file


class PageLogin:
    placeholder_login = "Логин или email"
    error_text = ".Textinput-Hint"
    button_phone = "[data-type='phone']"
    field_phone = "#passp-field-phone"

    def __init__(self, browser_fixture):
        self.browser_fixture = browser_fixture

    def login_wrong_user_name(self, data):
        page = self.browser_fixture
        page.goto(settings.url_test_env)
        field_login = page.get_by_placeholder(self.placeholder_login)
        field_login.click()
        field_login.fill(data)
        field_login.press("Enter")
        error_elem = page.locator(self.error_text)
        text = error_elem.text_content()
        if text == "Такой логин не подойдет":
            write_to_file("Test_login_wrong_user_name: successful ")
        else:
            write_to_file("Test_login_wrong_user_name: failed")

    def wrong_phone(self, data):
        page = self.browser_fixture
        page.goto(settings.url_test_env)
        phone_button = page.locator(self.button_phone)
        phone_button.click()
        phone_field = page.locator(self.field_phone)
        phone_field.click()
        phone_field.type(data)
        phone_field.press("Enter")
        text_error = page.locator(self.error_text)
        text_error = text_error.text_content()
        if text_error == "Недопустимый формат номера":
            write_to_file("Test_wrong_phone: successful")
        else:
            write_to_file("Test_wrong_phone: failed")

    def empty_field_login(self):
        page = self.browser_fixture
        page.goto(settings.url_test_env)
        field_login = page.get_by_placeholder(self.placeholder_login)
        field_login.click()
        field_login.press("Enter")
        text_error = page.locator(self.error_text)
        text_error = text_error.text_content()
        if text_error == "Логин не указан":
            write_to_file("Test_empty_field_login: successful")
        else:
            write_to_file("Test_empty_field_login: failed")

    def empty_field_phone(self):
        page = self.browser_fixture
        page.goto(settings.url_test_env)
        phone_button = page.locator(self.button_phone)
        phone_button.click()
        phone_field = page.locator(self.field_phone)
        phone_field.click()
        phone_field.fill(" ")
        phone_field.press("Enter")
        text_error = page.locator(self.error_text)
        text_error = text_error.text_content()
        if text_error == "Сервис не смог обработать запрос. Обновите страницу и попробуйте еще раз.":
            write_to_file("Test_empty_field_phone: successful")
        else:
            write_to_file("Test_empty_field_phone: failed")

    def user_does_not_exist(self, data):
        page = self.browser_fixture
        page.goto(settings.url_test_env)
        field_login = page.get_by_placeholder(self.placeholder_login)
        field_login.click()
        field_login.fill(data)
        field_login.press("Enter")
        error_elem = page.locator(self.error_text)
        text = error_elem.text_content()
        if text == "Нет такого аккаунта. Проверьте логин или войдите по телефону":
            write_to_file("Test_user_does_not_exist: successful")
        else:
            write_to_file("Test_user_does_not_exist: failed")
