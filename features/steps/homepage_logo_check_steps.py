import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@given('launch chrome browser')
def launchBrowser(context):
    print("Inside launchBrowser")
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@when('open swag labs homepage')
def openHomepage(context):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

@then('verify that logo present in the homepage')
def verifyLogo(context):
    status = context.driver.find_element(By.CLASS_NAME, "login_logo").is_displayed()
    assert status is True

@then('close the browser')
def closeBrowser(context):
    context.driver.close()
