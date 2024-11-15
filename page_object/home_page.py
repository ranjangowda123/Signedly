from playwright.sync_api import Page

class HomePage:
    def __init__(self,page:Page):
        self.page = page

    doc_button = "Documents"
    add_button = "#addDocFromDiv"
    doc_list = "//table[@class='table-list-view w-full bg-shadow-blur']/tbody/tr/td[2]/div/span"
    view_docu = "text = View Document"
    temp = "Templates"
    temp_button = ".add-document__btn"
    tem_list = "//table[@class='table-list-view w-full bg-shadow-blur']/tbody/tr/td[1]/div/span[1]"
    preview_docu = "Preview"
    close_btn = "img[alt = 'close-icon']"
    contact_btn = "Contacts"
    contact_lists = "//table[@class='table-list-view table-list-view--workflow w-full bg-shadow-blur']/tbody/tr/td[1]/div/h4"
    bulk_sending_btn = "Bulk Sending"
    bulk_list = "//table[@class='table-list-view w-full bg-shadow-blur']/tbody/tr/td/div/span"
    folder_btn = "text = Folders"
    folders_lists = "//table[@class='table-list-view table-list-view--workflow w-full bg-shadow-blur']/tbody/tr/td[1]"
    click_on_documents_text = "//span[text()='Documents']"
    workflow_lists = "//table[@class= 'table-list-view table-list-view--workflow w-full bg-shadow-blur']/tbody/tr/td[1]"

    def click_on_doc_button(self):
        self.page.get_by_text(self.doc_button).click()

    def click_on_add_button(self):
        self.page.locator(self.add_button).click()

    def document_lists(self):
        return self.page.locator(self.doc_list)

    def view_doc(self):
        self.page.locator(self.view_docu).click()

    def click_on_temp_btn(self):
        self.page.get_by_text(self.temp).click()

    def click_on_temp_creation(self):
        self.page.locator(self.temp_button).click()

    def temp_lists(self):
        return self.page.locator(self.tem_list)

    def preview_doc(self):
        self.page.get_by_text(self.preview_docu).click()

    def close_buton(self):
        self.page.locator(self.close_btn).click()

    def click_on_contact_text(self):
        self.page.get_by_text(self.contact_btn).click()

    def cont_list(self):
        return self.page.locator(self.contact_lists)

    def bulk_sending(self):
        self.page.get_by_text(self.bulk_sending_btn).click()

    def bulk_lists(self):
        return self.page.locator(self.bulk_list)

    def folder_button(self):
        self.page.locator(self.folder_btn).click()

    def folder_list(self):
        return self.page.locator(self.folders_lists)

    def click_on_doc_text(self):
        self.page.locator(self.click_on_documents_text).click()

    def workflow_list(self):
        return self.page.locator(self.workflow_lists)








