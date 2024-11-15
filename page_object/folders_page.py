import random

from playwright.sync_api import Page

class FoldersPage:

    def __init__(self,page:Page):
        self.page = page

    folder_create_btn = "text = Create New Folder"
    folder_value = "New Folder"
    folder_save = "div.modal__footer button:has-text('Create')"
    upload_doc =  "Upload"


    def click_on_create_fold_btn(self):
        self.page.locator(self.folder_create_btn).click()

    def folder_names(self):
        folder_name = f"Automated_Folder_Name_{random.randint(3,3000)}"
        self.page.get_by_placeholder(self.folder_value).fill(folder_name)
        self.page.locator(self.folder_save).click()
        return folder_name

    def click_on_upload_doc(self):
        self.page.get_by_role("button",name=self.upload_doc).click()






