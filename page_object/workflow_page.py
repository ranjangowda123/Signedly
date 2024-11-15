import random

from playwright.sync_api import Page
class WorkFlow:


    def __init__(self,page:Page):
        self.page = page


    work_text = "Workflow"
    create_work_text = "text = Create Workflow"
    work_name = "//input[@type='text']"
    work_email = "//input[@type='email']"
    work_save = ".btn--primary"
    workflow_name = "Title"
    save = "//div[@class='modal__footer flex justify-end gap-3']/button[2]"

    def click_on_work_text(self):
        self.page.get_by_text(self.work_text).click()

    def click_on_create_workflow(self):
        self.page.locator(self.create_work_text).click()

    def enter_on_workflow(self):
        workflow_name = f"Workflow_{random.randint(2, 2000)}"
        self.page.locator(self.work_name).fill(workflow_name)
        email = f"ranjanworkflow+{random.randint(1, 9999)}@gmail.com"
        self. page.locator(self.work_email).fill(email)
        self.page.locator(self.work_save).click()

    def enter_on_workflow_name(self):
        workflow_names = f"Automated_workflow_name_{random.randint(4, 2000)}"
        self.page.get_by_placeholder(self.workflow_name).fill(workflow_names)
        self.page.locator(self.save).click()
        return workflow_names




