import allure
from playwright.sync_api import Page
from page_object.home_page import HomePage
from page_object.prepage_page import PreparePage
from page_object.template_name import TemplateName
from page_object.upload_page import UploadFile

@allure.feature("Template Module")
@allure.story("Template Creation")

def test_template_creation(page:Page):
    home = HomePage(page)
    home.click_on_temp_btn()
    home.click_on_temp_creation()
    file = UploadFile(page)
    file.upload_document()
    page.locator(".loader").first.wait_for(state="hidden", timeout=100000)
    prepare = PreparePage(page)
    prepare.draggelement()
    prepare.click_on_next_button()
    temp =  TemplateName(page)
    template_name = temp.template_name_creation()
    print(template_name)
    page.locator(".loader").first.wait_for(state="hidden", timeout=50000)
    temp.enter_on_field().fill(template_name)
    page.locator(".loader").first.wait_for(state="hidden")
    temps = home.temp_lists()
    rows = temps.all()
    for row in rows:
        temp_values = row.text_content().strip()
        if temp_values == template_name:
            print("Ready To Click........")
            row.click()
            break
    page.locator(".loader").first.wait_for(state="hidden", timeout=50000)
    home.preview_doc()
    home.close_buton()

