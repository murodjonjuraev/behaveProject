# How we can pass parameters to the steps
# scenario outline, how to pass multiple parameters
from behave import *
from selenium import webdriver


@given('Launch Chrome browser')
def open_browser(context):
    # context.driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
    context.driver = webdriver.Chrome()


@when('Open orangeHRM homepage')
def open_orangehrm_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def username_password(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when('Click on login button')
def click_login(context):
    context.driver.find_element_by_id("btnLogin").click()


# @then('User must successfully login to the Dashboard page')
# in this step I need to login first and then copy xpath
# def logged_in(context):
# text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
# assert text == "Dashboard"
# context.driver.close()

@then('User must successfully login to the Dashboard page')
# in this step I need to login first and then copy xpath
def logged_in(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "test passed"


