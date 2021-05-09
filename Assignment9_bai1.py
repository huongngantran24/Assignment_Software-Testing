from selenium import webdriver
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)

driver.get ("http://practice.automationtesting.in/")

search = driver.find_element_by_name("q")
search.send_keys("http://practice.automationtesting.in/")
driver.close()