import asyncio
import os
import shutil
import pytest
import allure
from playwright.sync_api import sync_playwright, Page

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chromium")


@pytest.fixture(scope="function")
@allure.feature('Authentication')
def page(request):
    if asyncio.get_event_loop().is_running():
        raise RuntimeError("An asyncio event loop is running. Please use the sync API outside an async event loop.")
    browser_name = request.config.getoption("browser_name")
    with sync_playwright() as playwright:
        browser = getattr(playwright, browser_name).launch(headless=False, slow_mo=500)   # getattr() will give all 3 browsers
        # chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        # browser = playwright.chromium.launch(executable_path=chrome_path,headless=False,slow_mo=500)

        # ...........for mobile device...........
        #.......The ** is unpacking the dictionary pixel_5 and passing its keys and values as keyword arguments to browser.new_context().
        # pixel_5 = playwright.devices["iPhone 15 Pro Max"]
        # context = browser.new_context()
        # page = context.new_page()

        #..........for normal execution...............
        page = browser.new_page()
        qa_url = "https://qa.signedly.com/"
        prod_url = "https://www.signedly.com/"
        page.goto(prod_url)
        page.locator("text = Log In").first.click()
        page.get_by_label("Email").fill("ranjan+10@reckonsys.com")
        page.get_by_label("Password").fill("143792@Rn")
        page.locator("#kc-login").click()
        yield page
        print("Ready To Logout...........")
        page.wait_for_selector("#profileDownArrow" , state="visible", timeout=100000)
        page.locator("#profileDownArrow").click()
        page.get_by_text("Logout").click()
        page.close()

def test_setup(page):
    pass

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in Allure report on failure.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':  # Only after the test itself has run
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            try:
                # Access the page fixture from item._request
                page: Page = item._request.getfixturevalue('page')

                # Generate screenshot file name
                file_name = report.nodeid.replace("::", "_") + ".png"

                # Ensure the file path is correct
                screenshot_path = os.path.join(os.getcwd(), "screenshots", file_name)

                # Capture screenshot using Playwright's page.screenshot method
                _capture_screenshot(page, screenshot_path)

                # Attach screenshot to the Allure report
                with open(screenshot_path, "rb") as f:
                    allure.attach(f.read(), name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)

            except Exception as e:
                print(f"Error capturing screenshot: {e}")

def _capture_screenshot(page: Page, name: str):
    """Capture a screenshot with Playwright and save it to the specified file."""
    screenshots_dir = os.path.dirname(name)
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Capture the screenshot and save it to the file
    page.screenshot(path=name)
    print(f"Screenshot saved at {name}")



@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    # Define the allure-results directory
    allure_dir = os.path.join(os.getcwd(), 'allure-resultsss')
    if os.path.exists(allure_dir):
        shutil.rmtree(allure_dir)  # Delete the allure-results folder
    os.makedirs(allure_dir)  # Recreate the directory if necessary

