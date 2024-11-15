#
# from playwright.sync_api import sync_playwright
# from creds import email,password
#
# with sync_playwright() as playwright:
#     browser = playwright.firefox.launch(headless=False)
#     # Set realistic browser context with a User-Agent
#     context = browser.new_context(
#         user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         viewport={'width': 1366, 'height': 768},  # Set viewport size
#         locale='en-US',  # Set language to match the default for Chrome
#         timezone_id='Asia/Kolkata',  # Set a realistic timezone
#         permissions=["geolocation", "notifications"],  # Allow geolocation, notifications
#         ignore_https_errors=True  # Ignore SSL errors (sometimes useful)
#     )
#     # context = browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
#     page = context.new_page()
#     page.goto("https://mail.google.com/")
#     page.locator("#identifierId").fill(email)
#     page.get_by_text("Next").click()
#     page.wait_for_timeout(3000)
