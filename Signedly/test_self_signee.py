import allure
import pytest
from playwright.sync_api import Page
from page_object.add_signee_page import AddSignee
from page_object.home_page import HomePage
from page_object.prepage_page import PreparePage
from page_object.upload_page import UploadFile

@allure.feature("Sign Document Using Self Signee")
@allure.story("Document Self Signee")
# @pytest.mark.parametrize("iteration", range(1,251))
def test_selfsignee(page:Page):    # iteration
    # print(f"running iteration...{iteration}")
    home = HomePage(page)
    home.click_on_doc_text()
    home.click_on_add_button()
    file_upload = UploadFile(page)
    file_name, new_file_path = file_upload.upload_document()
    print(file_name)
    signee = AddSignee(page)
    signee.signee_page()
    page.locator(".loader").first.wait_for(state="hidden", timeout=100000)
    prepare = PreparePage(page)
    prepare.draggelement()
    prepare.elements_flow()
    prepare.click_on_next_button()
    prepare.click_on_accept_btn()
    page.locator(".loader").first.wait_for(state="hidden", timeout=50000)
    page.locator("(//div[@class='secondary-header__nav__item'])[2]").click()
    page.locator(".loader").first.wait_for(state="hidden", timeout=50000)
    doc_lists = home.document_lists()
    rows = doc_lists.all()
    for row in rows:
        doc_values = row.text_content().strip()
        if doc_values == file_name:
            print("Ready To Click........")
            row.click()
            break
    page.locator(".loader").first.wait_for(state="hidden", timeout=5000)
    home.view_doc()
    print("Self Signee Added Successfully")

