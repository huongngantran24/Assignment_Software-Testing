from selenium import webdriver
import time
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)
driver.maximize_window()

driver.get ("https://www.facebook.com/")
time.sleep(1)
titl= driver.current_url
print(titl)
try:
    assert 'Facebook' in driver.title
    print('Assertion test pass')
except Exception as e:
    print('Assertion test failed',format(e))

time.sleep(2)
driver.close()
