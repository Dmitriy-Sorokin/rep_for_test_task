import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(no_viewport=True)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        viewport_size = {"width": 1920, "height": 1080}
        page.set_viewport_size(viewport_size=viewport_size)
        yield page
        # context.tracing.stop(path="trace.zip")
        page.close()
        browser.close()
