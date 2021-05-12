from selenium import webdriver
import time
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)
driver.set_window_size(300,1000)

driver.get ("http://practice.automationtesting.in/")

try:
    assert 'Automation Practice Site' in driver.title
    print('Assertion test pass')
except Exception as e:
    print('Assertion test failed',format(e))

time.sleep(1)
driver.close()