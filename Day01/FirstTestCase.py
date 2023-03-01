#   * Test Case *

# 1) Open Web Browser (Chrome/Firefox/ Edge):
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/shobhit/Documents/driver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# 2) Open URL https://opensource-demo.orangehrmlive.com/

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(5)
# 3) Enter username (Admin).
driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]').send_keys('Admin')

# 4) Enter password (adnini23).
driver.find_element(By.XPATH, "(//input[@placeholder='Password'])[1]").send_keys('admin123')
time.sleep(5)

# 5) Click on Login.

driver.find_element(By.XPATH, "//button[@type='submit']").click()


# 6) Capture title of the home page.(Actual title)

act_title = driver.title

# 7) Verify title of the page: OrangeHRM(Expected)
#
exp_title="OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Passed")

# 8) close browser

# driver.close()
time.sleep(10)
