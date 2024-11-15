# import re
# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://qa.signedly.com/")
#     page.goto("https://qa.signedly.com/main/documents")
#     page.goto("https://accounts.signedly.com/realms/signedly-qa/protocol/openid-connect/auth?client_id=signedly-qa&redirect_uri=https%3A%2F%2Fqa.signedly.com%2Fmain%2Fdocuments&state=81e5dad0-bf7a-4c9e-9d55-f0750a71b0c3&response_mode=fragment&response_type=code&scope=openid&nonce=ca0f740c-104c-439e-83d7-7bb4ab7ea72f")
#     page.wait_for_load_state("networkidle")            # wait statement
#     page.get_by_label("Email").click()
#     page.get_by_label("Email").fill("ranjan+7@reckonsys.com")
#     page.get_by_label("Password").click()
#     page.get_by_label("Password").fill("Test@1234")
#     page.pause()
#     page.get_by_role("button", name="Sign In").click()
#     page.get_by_role("link", name="Contacts").click()
#     page.locator("div").filter(has_text="Add Contact").nth(3).click()
#     page.get_by_placeholder("eg. John", exact=True).click()
#     page.get_by_placeholder("eg. John", exact=True).fill("playwright_contact")
#     page.get_by_placeholder("eg. John", exact=True).press("Tab")
#     page.get_by_placeholder("eg. John@gmail.com").fill("playwright3@gmail.com")
#     page.get_by_role("button", name="Add Contact").click()
#     page.locator("#profileDownArrow").click()
#     page.get_by_text("Logout").click()
#     print("Test Execution is Passed.............")
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
#
#
#
#
#
#
#
