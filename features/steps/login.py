from playwright.sync_api import sync_playwright , expect
from behave import *

@given('I am in the login page')
def login_page(context):
    context.page.goto("https://qa.signedly.com/")


@when('I enter the credentials and click on login button')
def enter_credentials(context):
    context.page.get_by_label("Email").fill("ranjan+7@reckonsys.com")
    context.page.get_by_label("Password").fill("Test@1234")
    context.page.locator("#kc-login").click()


@then('homepage should be displayed with valid text')
def verify_homepage(context):
    message = context.page.locator(".add-document__heading")
    expect(message).to_have_text("Transform your document signing process with Signedly")
