from playwright.sync_api import Page

class AddSignee:

    def __init__(self,page:Page):
        self.page = page

    click_on_skip_this_step = "button.btn--secondary"

    def signee_page(self):
        self.page.locator(self.click_on_skip_this_step).click()




