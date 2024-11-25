# import allure
# import pytest
# from playwright.sync_api import Page
# from page_object.contact_page import ContactPage
# from page_object.home_page import HomePage
#
#
# @allure.feature("Contact Module")
# @allure.story("Contact Creation")
# def test_contact(page:Page):
#     home = HomePage(page)
#     home.click_on_contact_text()
#     contact = ContactPage(page)
#     contact.click_on_contact_button()
#     contact_name = contact.contact_pop_up()
#     page.locator(".loader").first.wait_for(state="hidden")
#     contact_list = home.cont_list()
#     rows = contact_list.all()
#     contact_added = False
#     for row in rows:
#         contact_values = row.text_content().strip()
#         if contact_values == contact_name:
#             contact_added = True
#             break
#     assert contact_added, f"Contact '{contact_name}'not added."
#     print("Contact Added Successfullyy")
#
