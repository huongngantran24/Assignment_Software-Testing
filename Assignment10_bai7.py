from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)
driver.maximize_window()

driver.get ("http://practice.automationtesting.in/")

butt1 = driver.find_element_by_id('menu-item-50')
butt1.click()
time.sleep(1)
mail = driver.find_element_by_id('reg_email')
mail.send_keys('tthngan.18it3@vku.udn.vn')
time.sleep(2)
passw = driver.find_element_by_id('reg_password')
passw.send_keys('tthngan18vkuudnvn')
time.sleep(2)

butt2 = driver.find_elements_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/font/font/font/font/input')
butt2.click()

try:
    assert 'My Account-Automation Practice Site' in driver.title
    print('Assertion test pass')
except Exception as e:
    print('Assertion test failed',format(e))

time.sleep(2)
driver.close()

