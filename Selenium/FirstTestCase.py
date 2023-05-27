from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("D:\driver\chromedriver.exe")
#
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/login")
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "email").send_keys("test@gmal.com")
driver.find_element(By.CLASS_NAME, "password").send_keys("123456")

driver.find_element(By.CLASS_NAME, "login-button").click()

actualTitle = driver.title
expectedTitle = 'nopCommerce demo store'

if actualTitle == expectedTitle:
    print("Login Test Passed")
else:
    print("Login Test Failed")

    driver.close()
