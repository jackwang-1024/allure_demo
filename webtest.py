from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.implicitly_wait(3)

url = "https://172.16.100.209/"

# url="https://www.baidu.com"
driver.get(url)
driver.implicitly_wait(30)

ele_gaoji = driver.find_element(By.ID, "details-button")
ele_gaoji.click()
ele_forward = driver.find_element(By.ID, "proceed-link")
ele_forward.click()
ele_username=driver.find_element(By.ID,"mat-input-0")
ele_username.send_keys("admin")
ele_password=driver.find_element(By.ID,"mat-input-1")
ele_password.send_keys("Hello123!")

#ele_login_btn=driver.find_element(By.CLASS_NAME,"login-button hcd-primary hcd-button")
ele_login_btn=driver.find_element(By.CSS_SELECTOR,'[class="login-button hcd-primary hcd-button"]')
ele_login_btn.click()

driver.find_element(By.XPATH,"//span[text()='存储管理']").click()
driver.find_element(By.XPATH,"//div[text()='创建卷']").click()

driver.find_element(By.XPATH,"//mat-dialog-content/descendant::input[@data-placeholder='请输入卷名称']").send_keys("abc003")
sleep(1)
driver.find_element(By.XPATH,"//input[@data-placeholder='请输入卷空间大小']").clear()
driver.find_element(By.XPATH,"//input[@data-placeholder='请输入卷空间大小']").send_keys("1")
sleep(1)
driver.find_element(By.XPATH,"//span[text()='GB']").click()
sleep(1)
driver.find_element(By.XPATH,"//span[text()='TB']").click()
sleep(1)
driver.find_element(By.XPATH,"//span[contains(text(),'创建卷') and @class='hcd-button-wrapper']").click()




