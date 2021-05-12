import time
from selenium import webdriver
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)
driver.maximize_window()

driver.get ("http://practice.automationtesting.in/")
sou= driver.page_source

print(sou)
try:
    assert 'Automation Practice Site' in driver.title
    print('Assertion test pass')
except Exception as e:
    print('Assertion test failed',format(e))

time.sleep(2)
driver.close()