from playwright.sync_api import Page
from Document_Upload.File_Generation import Files
from pathlib import Path

class UploadFile:

    def __init__(self,page:Page):
        self.page = page

    upload_file_button = "input[id = 'file-input']"
    click_on_next_button = "Next"


    def upload_document(self):
        file = Files()
        new_file_path = file.rename_downloaded_file()
        updated_file_name = Path(new_file_path)
        file_name = updated_file_name.name
        self.page.locator(self.upload_file_button).set_input_files(new_file_path)
        self.page.get_by_text(self.click_on_next_button).click()
        return file_name , new_file_path


