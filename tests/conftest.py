import pytest
from playwright.sync_api import sync_playwright
import os


@pytest.fixture(scope="session")
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1200, "height": 1200})
        page = context.new_page()
        yield page
        page.close()
        context.close()


@pytest.fixture(scope="session")
def file_cleaning():
    file_path = os.path.abspath(os.path.join(os.getcwd(), "artifacts/results.txt"))
    with open(file_path, "w") as file:
        file.write("")
