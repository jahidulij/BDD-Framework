from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@when('I open swag labs homepage')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

@when('enter username "{username}" and password "{pwd}"')
def step_impl(context, username, pwd):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(pwd)

@when('click on login button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()

@then('user must successfully login to the dashboard page')
def step_impl(context):
    verify_text = context.driver.find_element(By.XPATH, "//span[contains(text(),'Products')]").text
    assert verify_text == "PRODUCTS"
    context.driver.close()
