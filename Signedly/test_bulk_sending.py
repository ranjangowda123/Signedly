from playwright.sync_api import Page
#
# from page_object.bulk_sending_page import BulkSending
# from page_object.home_page import HomePage
# from page_object.prepage_page import PreparePage
# from page_object.template_name import TemplateName
# from page_object.upload_page import UploadFile
#
#
# def test_bulksending(page:Page):
#     home = HomePage(page)
#     home.bulk_sending()
#     home.click_on_add_button()
#     bulk = BulkSending(page)
#     bulk.click_on_create_button()
#     home.click_on_temp_creation()
#     upload = UploadFile(page)
#     upload.upload_document()
#     page.locator(".loader").first.wait_for(state="hidden",timeout=100000)
#     prepare = PreparePage(page)
#     prepare.draggelement()
#     prepare.click_on_next_button()
#     temp = TemplateName(page)
#     template_name = temp.template_name_creation()
#     print(template_name)
#     page.locator(".loader").first.wait_for(state="hidden", timeout=50000)
#     home.bulk_sending()
#     home.click_on_add_button()
#     page.locator(".loader").first.wait_for(state="hidden",timeout=20000)
#     template_list = bulk.click_on_inside_template()
#     rows = template_list.all()
#     for row in rows:
#         bulk_values = row.text_content().strip()
#         if bulk_values == template_name:
#             use_template_button = page.locator(f"//span[text()='{bulk_values}']/ancestor::tr//button[text()='Use Template']")
#             use_template_button.wait_for(state="attached",timeout=5000)
#             use_template_button.click()
#             break
#     prepare.click_on_next_button()
#     bulk.upload_csv()
#     prepare.click_on_next_button()
#     prepare.click_on_next_button()
#     bulk.enter_on_subject()
#     prepare.click_on_next_button()
#     bulk_list = home.bulk_lists()
#     bulks = bulk_list.all()
#     for bulkss in bulks:
#         bulks_values = bulkss.text_content().strip()
#         if bulks_values == template_name:
#             bulkss.click()
#     home.preview_doc()