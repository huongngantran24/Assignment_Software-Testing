from selenium import webdriver
import time
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)
driver.maximize_window()

driver.get ("https://www.facebook.com/")
time.sleep(1)
titl= driver.current_url
print(titl)

time.sleep(2)
driver.close()
