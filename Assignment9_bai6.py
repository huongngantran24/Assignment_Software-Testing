import time
from selenium import webdriver
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)
driver.maximize_window()

driver.get ("http://practice.automationtesting.in/")
sou= driver.page_source

print(sou)

time.sleep(2)
driver.close()