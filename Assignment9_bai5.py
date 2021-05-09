from selenium import webdriver
import time
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)
driver.maximize_window()

first_page = "http://www.google.com"
second_page = "https://www.facebook.com/"
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver.get(first_page)
time.sleep(1)
driver.execute_script("window.open('" + second_page +"');")

titl= driver.current_url.title
print(titl)
time.sleep(1)
driver.close()
