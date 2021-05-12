from selenium import webdriver
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)
driver.maximize_window()

driver.get ("http://practice.automationtesting.in/")
titl= driver.title
print(titl)

try:
    assert 'Automation Practice Site' in driver.title
    print('Assertion test pass')
except Exception as e:
    print('Assertion test failed',format(e))

driver.close()