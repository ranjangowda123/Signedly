# from playwright.sync_api import sync_playwright
#
# playwright = sync_playwright().start()
# #lauch browser
# # by default it will be in headless mode as True we need to change to false
# # to see our execution bit slow use slow_mo
# browser = playwright.chromium.launch(headless=False, slow_mo=1000)
# # open new page
# page = browser.new_page()
# # go to the page which we want...............
# page.goto("https://qa.signedly.com/")
# email_button = page.get_by_role('textbox',name='Email')
# # email_button.click()...............
# email_button.fill("ranjan+7@reckonsys.com")
# password_button = page.get_by_label('Password')
# password_button.fill("Test@1234")
# click_on_sign_button = page.get_by_role('button',name='Sign In')
# click_on_sign_button.click()
# # to get the url............
# print('Sign In',page.url)
# #close the browser
# browser.close()
#
#
# import random
#
# from playwright.sync_api import sync_playwright
# from time import perf_counter
#
# # def loadonly(page):
# #     print("Page is Fully Loaded:",page)
# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False,slow_mo=500)
# page= browser.new_page()
# print("Page loading..........")
# start= perf_counter()
# # page.on("load",loadonly)                       # this will help us to wait for page is fully loaded
# page.goto("https://qa.signedly.com/", wait_until="load")
# # page.remove_listener("load",loadonly)          # if we add on(), this method is required to remove once it is done
# timetaken = perf_counter()-start
# print(f"Page loaded............{round(timetaken,2)}sec")
# page.get_by_label("Email").fill("ranjan+7@reckonsys.com")
# page.get_by_label("Password").fill("Test@1234")
# page.get_by_role("button",name="Sign In").click()
# # page.get_by_role("link",name="Contacts").click()
# # page.locator("span.add-document__btn__content").click()
# # # page.wait_for_selector("div.modal__container")
# # contact_name = f"Playwright_Contact_{random.randint(1,1000)}"
# # page.locator("xpath=//input[@name = 'name']").fill(contact_name)
# # page.locator("xpath=//input[@name = 'email']").fill("playwright@gmail.com")
# # page.locator("xpath=//button[@type='submit']").click()
# page.locator("#addDocFromDiv").click()
# file_input = page.locator("#file-input")
# file_input.set_input_files(r"C:\Users\VMRanjan\Downloads\Selenium_499.pdf")
# page.get_by_role("button",name="Next").click()
# page.get_by_role("button",name="Skip this Step").click()
# source_element = page.locator("xpath = //li[@class = 'drag-and-drop-comp-list right']")
# if source_element.is_visible():
#     # Get the bounding box
#     box = source_element.bounding_box()
#
#     if box:
#         # Dragging by 100 pixels to the right and 50 pixels down
#         page.mouse.move(box['x'] + box['width'] / 2, box['y'] + box['height'] / 2)
#         page.mouse.down()
#         page.mouse.move(box['x'] + box['width'] / 2 + 100, box['y'] + box['height'] / 2 + 50)
#         page.mouse.up()
#
# page.get_by_placeholder("Type here").fill("Ranjan")
# page.get_by_role("button",name="Next").click()
# page.get_by_role("button",name="Accept and Sign").click()
#
#
# # contact_elements = page.locator("xpath = //table[@class='table-list-view table-list-view--workflow w-full bg-shadow-blur']/tbody/tr/td/div/h4")
# # contact_lists = contact_elements.all()  # this will keep all the matching elements
# # for contact in contact_lists:
# #     contact_name_text = contact.text_content()
# #     print(contact_name_text)
# #     if contact_name_text == contact_name:
# #         print("Contact Added Successfully....")
# #         break
# # else:
# #     print("Contact is Not Added")
# browser.close()
#
