import random
from tempfile import template

from playwright.sync_api import Page

class TemplateName:

    def __init__(self,page:Page):
        self.page = page

    temp_name = "input[placeholder='Template Title']"
    drop = ".css-1xc3v61-indicatorContainer"
    select_option = "//div[@class=' css-1vmpdro']/div[1]"
    save_btn = "Save"
    search_field = "Search Templates"


    def template_name_creation(self):
        template_name = f"Automated_Template_Name_{random.randint(7, 5000)}"
        print("name is........", template_name)
        self.page.locator(self.temp_name).fill(template_name)
        self.page.locator(self.drop).click()
        self.page.locator(self.select_option).click()
        self.page.get_by_role("button",name=self.save_btn).click()
        return template_name

    def enter_on_field(self):
        return self.page.get_by_placeholder(self.search_field)



