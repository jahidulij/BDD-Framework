from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@given('OHRM I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@when('OHRM I open OrangeHRM homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()

@when('OHRM enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.ID, "txtUsername").clear()
    context.driver.find_element(By.ID, "txtUsername").send_keys(user)
    context.driver.find_element(By.ID, "txtPassword").clear()
    context.driver.find_element(By.ID, "txtPassword").send_keys(pwd)

@when('OHRM click on login button')
def step_impl(context):
    context.driver.find_element(By.ID, "btnLogin").click()
    context.driver.implicitly_wait(5)

@then('OHRM user must successfully login to the dashboard page')
def step_impl(context):
    try:
        val = context.driver.find_element(By.XPATH, "//b[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if val == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
