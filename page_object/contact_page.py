import random
import allure

from playwright.sync_api import Page

class ContactPage:

    def __init__(self, page: Page):
        self.page = page

    cont_btn = ".add-document__btn__content"
    cont_name = "input[name='name']"
    cont_email = "input[name='email']"
    add_btn = "Add Contact"

    def click_on_contact_button(self):
        self.page.locator(self.cont_btn).click()

    @allure.step("Filling The Contacts....")
    def contact_pop_up(self):
        contact_name = f"Automated_contact_name_{random.randint(5, 2000)}"
        email = f"ranjancontact+{random.randint(1, 9999)}@gmail.com"
        self.page.locator(self.cont_name).fill(contact_name)
        self.page.locator(self.cont_email).fill(email)
        self.page.get_by_role("button", name=self.add_btn).click()
        return contact_name
