from playwright.sync_api import Page

class BulkSending:
    def __init__(self,page:Page):
        self.page = page

    click_on_create_btn  = "Create a new Template"
    bulk_inside_lists = "//table[@class='table-list-view w-full bg-shadow-blur']/tbody/tr/td/div/span[1]"
    csv = "input[id = 'file-input']"
    subject =  "Type subject here"


    def click_on_create_button(self):
        self.page.get_by_role("button",name=self.click_on_create_btn).click()

    def click_on_inside_template(self):
        return self.page.locator(self.bulk_inside_lists)

    def upload_csv(self):
        self.page.locator(self.csv).fill(r"C:\Users\VMRanjan\Downloads\csvfile.csv")

    def enter_on_subject(self):
        self.page.get_by_placeholder(self.subject).fill("Using Playwright")



