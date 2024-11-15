# ............................COMMANDS TO INSTALL PLAYWRIGHT....................
# pip install pytest-playwright
# playwright install---------to install browser
# pip show playwright
# playwright list
#--------------------------------------------------------------------------------------------------------------------------------------------
#..............There are 2 ways to run with code and with codegen(auto)
# playwright codegen https://example.com
# Headless and Headed mode
# pause()------ it will stop the script

#---------------------------------------------------------------------------------------------------------------------------------------------
# ....................To launch the browser we need Playwright's API ,
# There are 2 API's, Synchronous and Asynchronous APIs provide different ways to interact with browsers and pages
    # synchronous---------- one is just like normal python code
    # Asynchronous---------- one uses async and await keyword to control the flow of execution
#-------------------------------------------------------------------------------------------------------------------------------------------

#....................Different ways of locating the element...........................
# get_by_role()-----ex------page.get_by_role('link'),name="Docs").click()
# get_by_placeholder()-------ex--------page.get_by_placeholder("Enter Mail").click()
# get_by.text()-------------ex---------page.get_role_text("smallbutton").click()
#------------------for text we can also add using contains() where we want only fineprint text, get_by.text("fineprint"),exact=Flase, or exact=True if we want exact text
# get_by_label()------------ex----------
# get_by_title()-----------ex----------page.get_by_titile("attribute").click()
# get_by_alt_text().........used only to locate for image---------if there is any image when we inspect we will get an alt text based on that we can perform actions

#---------------------------------------------------------------------------------------------------------------------------------------------
# .....................To Get The URL From Web Address...............................
# page.get_by_role("link",name="Forgot Password?").click()
#     print("Forgot Password?",page.url)
#-----------------------------------------------------------------------------------------------------------------------------------------------
# ...........We Can Find .........CSS SELECTORS...............By Using..........
#                    1. Classname
#                    2. ID
#                    3. Tagname
#                    4. Attribute/Value

# Class Name
# Syntax----------page.locator("Tagname.Class-Attributevalue").click()

# Tagname
# page.locator("css=tagname").click() -----------<h1>Default<h1>

# ID
# Syntax-------page.locator("tagname#IDvalue").click()

# Attribute/value
# page.locator("tagname[attributevalue]").click()...........singleword-----------Attribute
#.................OR.....................
# page.locator("tagname[atrributename='attributevalue']").click()
#------------------------------------------------------------------------------------------------------------------------------------------------
#......................To Traverse Using CSS Selector............................

#-------------if we need to traverse from parent to child in CSS,
# ---------------ex--------tagname.classname(giveonespace)tag.classname.classname ( based on our requirement) ---bottom-down

#.....................suppose after inscepting if we found 2.......................
# ...........ex..........tagname.classname,-here we got 1 of 2------- search for the parent which we want then
#............................tagname.classname > tagname.classname(above one) ............it searches for ul which is under div tag

# .....................CSS Pseudo Class.....................
#..............ex................page.locator("tagname:text('textvalue')").click()
# ...............if there is same word present like Docs and Document and want only Docs to be selected-
# -------------.page.locator("tagname:text-is('textvalue')").click()

#---------------------------------------------------------------------------------------------------------------------------------------------------

#     table.table-list-view tbody tr:first-of-type td div.items-center span --------for the first one
#       table.table-list-view tbody tr:nth-of-type(n) td div.items-center span------------for 1,2nd,3rd etcccccc


#.........if we want to heighlight only visible in the application
# ...............ex..............page.locator('tagname.class-Attributevalue:visible').click()


#...........................if there are multiple matchesss we can select based on nth match(), like 1st one / 2nd one etc.........................
# >>> page.locator(':nth-match(div.secondary-header__nav__item,1)').highlight()

# using text
# >>> page.locator(':nth-match(div:text("secondary-header__nav__item"),2)').highlight()

#--------------------------------------------------------------------------------------------------------------------------------------------

#..............................USING__________XPATH..............................................
# .........here (xpath text is optional)

# >>> page.locator("xpath=//div[@id='addDocFromDiv']").click()  -- xpath by attribute 1

# >>> page.locator("//input[@readonly]").highlight()-------using attribute only , which will be a single word

# >>> page.locator("//div[@id='addDocFromDiv']").click()  ------using both attribute name and value--------------

# >>> page.locator("//div[text()='Pick a Template']").click()------xpath by text()

# >>> page.locator("//div[contains(text(),'Cloud')]").click()------------xpath by contains   or using attribute name and value..............("//input[contains(@id, 'email')]")

# .............so if there are 5 primary buttons and if we need to click on 2nd primary button using get_by_role and nth
# page.locator.get_by.role('button',name='Primary').locator("nth=0).click() for 1st,2nd,3rd index etc

#...................................OR......................
# page.locator('tagname').locator('nth=0').click()

# we can combine/append multiple locators with css/get.by.role etc...............also

# if we need to traverse from child to its main parent use ".."
# ..........ex page.get_by_label("Email Address").locator("..").click()

#...............Based on ID Locator......................................................
# page.locator("#idvalue").click()
# page.locator("tagname[id = 'idvalue']").click()

# use visible using locator
# page.locator('tagname.class-Attributevalue').locator('visible=True').click()


#..............if there are multiple text and we want only specided text to be visible
# ....ex................page.get.by.role("heading").filter(has_text="heading").click()
# ....................Heightlight using input fields
# .........ex........page.get.by.role("heading").filter(has=page.get_by.label("Password").click()

# ...............if there are 2 elements matching and if we want first or last we can use..............
# ...........ex............page.get.by.role("button",name=buttonvalue).first /last etc
#-----------------------------------------------------------------------------------------------------------------------------------------------

# ...........................MOUSE ACTIONS...................

# .....................firstone = page.locator('div.secondary-header__nav__item').nth(2)
# .....................firstone.dblclick(delay=500)----------For DOUBLE click
# .....................firstone.click(button="right") -----------for right click
# .....................firstone.click(modifiers=["Shift","Control"])-------if there are 10 words if we need to select 5 then we use shift
# .....................there are other mainly used keywords like Alt,control,Windowskey
# .....................firstone.hover()------To Mouse Hover

#------------------------------------------------------------------------------------------------------------------------------------------

#..................Fill Input Fields...............
# To enter values in input field use-----------fill() or type()
# >>> inputfield.type("Ranjan",delay = 450), while entering the values like human is actually typing

#...........To get the value from the field which is already entered----------using input_value()

#----------------------------------------------------------------------------------------------------------------------------------------

#...............Radios/checkbox/switches
#check() OR set_checked(True)-----------------To verify whether it is checked or not
#uncheck() OR set_checked(False)--------------To verify whether it is checked or not
# to verify it is checked or not use variable of that checkbox , variablename.is_checked()

#--------------------------------------------------------------------------------------------------------------------------------------------

#............Select option from option menu...............
# if it is select tag use ------------select_option("mention value here") like page.get_by_label(select_option("4"))
# we can select multiple options also -----------select_option(['2','4'])

#------------------------------------------------------------------------------------------------------------------------------------------

# ............Dropdown menu...........
# first inspect on click using its label value or id etc
# second inspect on values --------if there are more try giving visible since it is clicked then try giving a:text('textname')
# if you want first or last or anything in middle use first/last or nth("givevalue")
#..........ex.........page.locator("tagname.class-attributevalue:visible a:text("textvalue")").last/first or nth('give value')

#-------------------------------------------------------------------------------------------------------------------------------------------

# ...........................Upload Files................1st approach....................
#...................file_input = page.locator("#file-input")  or by get_by_label anything
# ...................file_input.set_input_files(r"C:\Users\VMRanjan\Downloads\jshjnjnc.pdf")

# ..............................2nd Approach......................
# if there is a situation where when we click on normal button and if i got window pop to upload file then we should handel like this
# with page.expect_file_chooser() as fc_info:  when we click on upload element the file chooser window pop up will be stored as fc_info
# filechooser = fc_info.value
# filechooser.set_files("upload file name here")

#--------------------------------------------------------------------------------------------------------------------------------------------------

# ..................keyboard actions...........
# inspect on element------store it in one variable
# variable.press("KeyR")
# variable.press("Shift+KeyD")

# .....................waiting...................
# when we need to wait based on time use click(timeout = 2000)
# we can forcefully wait for the element click(force=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------
# ........................................................Page navigation events............................................................

# ............if we want to know the time difference between each step we should configure the below one.............
#............from time import perf_counter..............
# perf_counter Function:
# This specific function is used to measure how long a piece of code takes to run.
# It gives you a high-precision timer, which means it can measure time very accurately, down to fractions of a second.
# Why Use perf_counter?
# Performance Measurement: If you want to see how long your code takes to execute (for example, to optimize performance), you use perf_counter.
# Simple Example
#------------------------------------------------------------------------------------------------------------------------------------------
# .................custom waiting...........
# fetch the variable and ------wait_for(timeout = 30000) by default 30 sec it will wait
# we can also wait for its state waits like wait_for(state= visible/stable etc)
# first = page.locator("td.divmff")--------recommended
# first.wait-for() 0r directly page.wait_for_selector(selcetor = "td.divmff")

#......page.wait_for_load_state():
# This method can be called after navigation to wait for the page to reach a certain load state.
# You can use it to wait for "load", "domcontentloaded", or "networkidle".

# ............page.wait_for_selector():
# To wait for specific elements to appear or be visible on the page after navigation.

# page.wait_for_timeout():   time.sleep()
# To simply wait for a specified amount of time, although this is not recommended
#  as it does not ensure that the page is fully loaded.

# page.goto("https://qa.signedly.com/")
# page.wait_for_load_state("load")

#------------------------------------------------------------------------------------------------------------------------------------------------------
#....................Event listeners...............just like log

# def loadonly(page):
#     print("page loaded:",page)
# page.on("load",loadonly)
# page.goto("https://qa.signedly.com/", wait_until="load")
# Common Playwright Events
# Page Events:
# load: Fired when the page has fully loaded (including all resources).
# domcontentloaded: Fired when the initial HTML document has been completely loaded and parsed, without waiting for stylesheets, images, and subframes to finish loading.
# framenavigated: Fired when a frame has navigated to a new URL.
# request: Fired when a request is made.
# response: Fired when a response is received for a request.
# console: Fired when a message is logged to the browser’s console.
# Browser Context Events:
# close: Fired when the context is closed.
# page: Fired when a new page is created within the context.
# Dialog Events:
# dialog: Fired when a dialog (like an alert, confirm, or prompt) is shown.

#-------------------------------------------------------------------------------------------------------------------------------------------
# ................................Keyboard and Mouse Events...............................................:
#
# keydown: Fired when a key is pressed down.
# keyup: Fired when a key is released.
# mousedown: Fired when a mouse button is pressed down.
# mouseup: Fired when a mouse button is released.

# Network Events:
#
# requestfailed: Fired when a network request fails.
# requestfinished: Fired when a network request finishes successfully.

#---------------------------------------------------------------------------------------------------------------------------------------------

# ................Handling Alret/Confirm popups.............
# ----------if toast has only one button directly click on that----------

# .........if it has 2 buttons..........................use below one
# def one(dialog):
#     dialog.dismiss()
#     dialog.accept("dhbj")----------if we are sending somthing inside a pop up
# page.on("dialog",one)
# pop_up = page.get_by_text("Show confirm box")
# pop_up.click()
#----------------------------------------------------------------------------------------------------------------------------------------------

#.............................................State() features.............................................
# In Playwright, the state parameter used with methods like wait_for() can take various values that indicate the visibility or presence state of an element. Here’s a brief explanation of each state:
#
# visible: Waits until the element is visible on the page. This means that the element is not only present in the DOM but also has a computed style that makes it visible (e.g., not hidden by CSS, not collapsed, etc.).
#
# hidden: Waits until the element is no longer visible on the page. This is useful for waiting for loaders, modals, or any elements that should disappear before continuing with further actions.
#
# attached: Waits until the element is attached to the DOM. This means the element exists in the document but may or may not be visible. This is useful if you want to ensure an element is in the DOM before interacting with it.
#
# detached: Waits until the element is removed from the DOM. This state is useful when you expect an element to be removed after a certain action, such as a dialog closing or a notification disappearing.
#
# When to Use Each State:
# Use visible: When you want to ensure that an element is ready for user interaction (like clicking or typing).
#
# Use hidden: When you want to wait for elements like loading spinners or pop-ups to disappear before proceeding.
#
# Use attached: When you want to make sure an element is present in the DOM before performing actions or checks on it, regardless of its visibility.
#
# Use detached: When you want to confirm that an element has been removed from the DOM after an action (like a dialog that closes).

#---------------------------------------------------------------------------------------------------------------------------------------------------
# .............................Download files and save in our desired location using Playwright.......................

#   img = page.get_by_role("link", name="give the name")
#     with page.expect_download() as download_info:
#         img.click()
#     download  = download_info.value
#     download.save_as("moon.jpg")

#-----------------------------------------------------------------------------------------------------------------------------------------------
#..............................Asynchronous....................
# import asyncio
# from playwright.async_api import async_playwright
#
#
# async  def main():
#     async with async_playwright() as playwright:
#         browser = await playwright.chromium.launch()
#         page = await browser.new_page()
#         await page.goto("")
# asyncio.run(main())----------------to run 

#--------------------------------------------------------------------------------------------------------------------------------------------------------

# ...........................Other Wait Methods........................................still moreeeeeeeeee
# summary of Methods to Wait for Elements:

# wait_for_selector(): Wait for an element to be attached, visible, enabled, etc. It's one of the most common and flexible methods.
# wait_for_load_state(): Wait for the page to reach a specific load state (e.g., load, domcontentloaded, networkidle).
# wait_for_event(): Wait for an event to occur, like a download, navigation, or dialog.
# wait_for_function(): Wait for a custom JavaScript condition to evaluate to true.
# wait_for_timeout(): Wait for a fixed amount of time (not commonly used for waiting on elements directly).
# wait_for_navigation(): Wait for page navigation to complete (e.g., after clicking a link).
# locator.wait_for(): Wait for an element (locator) to reach a specific state.
# expect() (in Playwright Test framework): Wait for and assert conditions for locators.

#...................................................... When to Use Which Method:
# Use wait_for_selector() when you're waiting for specific element conditions (attached, visible, enabled).
# Use wait_for_function() when you need to wait for a JavaScript condition.
# Use wait_for_event() when you're waiting for events like download or dialog.
# Use wait_for_load_state() for page load-related waits.
# Use locator.wait_for() when working with locators for more fine-grained control over waiting.
# I hope this helps! Let me know if you need further clarification.

#--------------------------------------------------------------------------------------------------------------------------------------------
# TO install playwright pytest plugin
#................. pip install pytest-playwright

#-----------------------------------------------------------------------------------------------------------------------------------------------
#     page.screenshot(path="screen.jpg")

#-------------------------------------------------------------------------------------------------------------------------------------------------
# ..............To record a video..................................
# in conftest class
#   # context = browser.new_context(record_video_dir="video/")     # to record a test video
#         # page = context.new_page()
#         # context.close() below yield



#   # def test_selfsignee(browser_and_page:tuple[Browser,Page]):
#     # browser,page  = browser_and_page     # unpacking a tuple returned by conftest file

#------------------------------------------------------------------------------------------------------------------------------------------


# allure reports command
# https://github.com/allure-framework/allure2/releases/tag/2.31.0
# add bin to path
# download package allure-pytest in pycharam
# pip install allure-pytest
# pytest --alluredir=allure-results
# allure serve allure-results

# command to open jenkis
# java is required
# java -jar jenkins.war
# java -jar jenkins.war --httpPort=8080