import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qa.signedly.com/")
    page.goto("https://qa.signedly.com/main/documents")
    page.goto("https://accounts.signedly.com/realms/signedly-qa/protocol/openid-connect/auth?client_id=signedly-qa&redirect_uri=https%3A%2F%2Fqa.signedly.com%2Fmain%2Fdocuments&state=d91f0ba9-4d87-40c3-a6a5-5ff64d3cea2c&response_mode=fragment&response_type=code&scope=openid&nonce=71aac433-ea23-4e57-8217-8478506a01cd")
    page.wait_for_load_state("networkidle")

    page.get_by_label("Password").click()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Test@1234")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("link", name="Contacts").click()
    page.get_by_text("Add Contact").click()
    page.get_by_placeholder("eg. John", exact=True).click()
    page.get_by_placeholder("eg. John", exact=True).fill("playwright")
    page.get_by_placeholder("eg. John@gmail.com").click()
    page.get_by_placeholder("eg. John@gmail.com").fill("playwright@gmail.com")
    page.get_by_role("button", name="Add Contact").click()
    page.locator("body").press("ControlOrMeta+Shift+S")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
