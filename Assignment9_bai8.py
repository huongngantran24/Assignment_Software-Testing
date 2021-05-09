from selenium import webdriver
import time
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)

driver.get ("https://the-internet.herokuapp.com")

butt1 = driver.find_element_by_link_text('Form Authentication').click()

time.sleep(1)

usname = driver.find_element_by_id('username')
usname.send_keys('tomsmith')

time.sleep(2)
passw = driver.find_element_by_id('password')
passw.send_keys('SuperSecretPassword!')

time.sleep(1)
butt2 = driver.find_elements_by_name("fa fa-2x fa-sign-in").click()
titl= driver.title
print(titl)

time.sleep(10)

driver.close()

