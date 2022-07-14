# For practice purposes only

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.implicitly_wait(5)
status = driver.find_element(By.CLASS_NAME, "login_logo").is_displayed()
print(status)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
status = driver.find_element(By.XPATH, "//div[@id='divLogo']//img").is_displayed()
verify_text = driver.find_element(By.XPATH, "//span[contains(text(),'Products')]").text
print(verify_text)

