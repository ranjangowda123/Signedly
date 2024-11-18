# import allure
# from playwright.sync_api import Page
# from page_object.add_signee_page import AddSignee
# from page_object.folders_page import FoldersPage
# from page_object.home_page import HomePage
# from page_object.prepage_page import PreparePage
# from page_object.upload_page import UploadFile
#
# @allure.feature("Folder Creation Document Upload Self Signee")
# @allure.story("Folder Creation")
# def test_folder_creation(page:Page):
#     home = HomePage(page)
#     home.folder_button()
#     fold = FoldersPage(page)
#     fold.click_on_create_fold_btn()
#     folder_name = fold.folder_names()
#     page.locator(".loader").first.wait_for(state="hidden", timeout=50000)
#     print("Folder Name is:", folder_name)
#     folder_listt = home.folder_list()
#     rows = folder_listt.all()
#     for row in rows:
#         fold_values = row.text_content().strip()
#         if fold_values == folder_name:
#             row.click()
#             break
#     fold.click_on_upload_doc()
#     file_upload = UploadFile(page)
#     file_name, new_file_path = file_upload.upload_document()
#     print(file_name)
#     signee = AddSignee(page)
#     signee.signee_page()
#     page.locator(".loader").first.wait_for(state="hidden", timeout=100000)
#     prepare = PreparePage(page)
#     prepare.draggelement()
#     prepare.elements_flow()
#     prepare.click_on_next_button()
#     prepare.click_on_accept_btn()
#     page.locator(".loader").first.wait_for(state="hidden", timeout=50000)
#     page.locator("(//div[@class='secondary-header__nav__item'])[2]").click()
#     page.locator(".loader").first.wait_for(state="hidden", timeout=50000)
#     doc_lists = home.document_lists()
#     rows = doc_lists.all()
#     for row in rows:
#         doc_values = row.text_content().strip()
#         combine = f"{folder_name}/{file_name}"
#         if doc_values == combine:
#             print("Ready To Click........")
#             row.click()
#             break
#     page.locator(".loader").first.wait_for(state="hidden", timeout=50000)
#     home.view_doc()
#     print("Folder Added Successfully")