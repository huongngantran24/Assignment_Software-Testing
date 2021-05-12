from selenium import webdriver
import time
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)
driver.maximize_window()

driver.get ("http://practice.automationtesting.in/")

time.sleep(2)
driver.close()