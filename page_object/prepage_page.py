from playwright.sync_api import Page,TimeoutError


class PreparePage:
    def __init__(self,page:Page):
        self.page = page

    source_elements = "li.drag-and-drop-comp-list.right:has(p:has-text('Text'))"
    enter_on_element = "Type here"
    click_on_next = "Next"
    click_on_accept = "Accept and Sign"


    def draggelement(self):
        print("Drag method called.........")
        try:
            warning_toast = self.page.locator(".Toastify__toast--warning").nth(0)
            warning_toast.wait_for(state="visible",timeout=5000)
            if warning_toast.is_visible():
                print("Warning toast is  visible, refreshing the page.")
                self.page.reload()
        except TimeoutError:
            print("Warning toast did not appear continuing the script")
        try:
            print("Locating the source element for drag-and-drop...")
            self.page.locator(".loader").first.wait_for(state="hidden", timeout=100000)
            source_element = self.page.locator(self.source_elements)
            source_element.wait_for(state="visible", timeout=100000)
            box = source_element.bounding_box()
            if box:
                self.page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
                self.page.mouse.down()
                self.page.mouse.move(box["x"] + 300, box["y"] + 400)
                self.page.mouse.up()
        except TimeoutError:
            print("Element Is Not Dragged.....!")

    def elements_flow(self):
        self.page.get_by_placeholder(self.enter_on_element).fill("Using Playwright")

    def click_on_next_button(self):
        self.page.get_by_role("button",name=self.click_on_next).click()

    def click_on_accept_btn(self):
        self.page.get_by_role("button",name=self.click_on_accept).click()




