from selenium import webdriver
import time
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)
driver.set_window_size(300,1000)

driver.get ("http://practice.automationtesting.in/")
time.sleep(1)
driver.close()