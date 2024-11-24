import random
import allure
from playwright.sync_api import Page

from page_object.home_page import HomePage
from page_object.workflow_page import WorkFlow


@allure.feature("Workflow Module")
@allure.story("Workflow Creation")
def test_workflow(page:Page):
    work = WorkFlow(page)
    work.click_on_work_text()
    work.click_on_create_workflow()
    work.enter_on_workflow()
    workflow_names = work.enter_on_workflow_name()
    home = HomePage(page)
    workflow_lists = home.workflow_list()
    rows = workflow_lists.all()
    for row in rows:
        work_values = row.text_content().strip()
        if work_values == workflow_names:
            row.click()
            break
    print("Workflow Created Successfully")
