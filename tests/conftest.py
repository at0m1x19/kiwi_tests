import os

import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from objects.page_objects.home_page import HomePage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)
        if page:
            try:
                screenshot_bytes = page.screenshot()
                allure.attach(
                    screenshot_bytes,
                    name="Screenshot on Failure",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Failed to take screenshot: {e}")


@pytest.fixture(scope="session", autouse=True)
def load_env_variables():
    """Load environment variables from a .env file at the start of the test session."""
    load_dotenv()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        headless = os.getenv("HEADLESS", "True").lower() == "true"

        browser = playwright.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def homepage(page):
    return HomePage(page)
