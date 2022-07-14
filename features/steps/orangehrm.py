from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



@given('OH launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@when('OH open OrangeHRM homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('OH verify that logo present in the homepage')
def step_impl(context):
    status = context.driver.find_element(By.XPATH, "//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then('OH close the browser')
def step_impl(context):
    context.driver.close()
