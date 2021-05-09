from selenium import webdriver
import time
chrome_drive_path="C:\Development\chromedriver"
driver = webdriver.Chrome(chrome_drive_path)

driver.get ("https://itmscoaching.herokuapp.com/form?fbclid=IwAR1uF-Ttcz7rK3Ck8hImqfhEz2rqJI3ScQkD09oc4hPMWMSyVvFu5c30G6E")
time.sleep(2)

fname = driver.find_element_by_id('first-name')
fname.send_keys('Binh')
time.sleep(2)

lname = driver.find_element_by_id('last-name')
lname.send_keys('Nguyen')

time.sleep(2)
job = driver.find_element_by_id('job-title')
job.send_keys('Tester')

time.sleep(2)
driver.find_element_by_css_selector("input#radio-button-3").click()

time.sleep(2)
driver.find_element_by_css_selector("input#checkbox-2").click()

time.sleep(2)
yr = driver.find_element_by_id('select-menu')
yr.send_keys('5-9')

time.sleep(2)
dt = driver.find_element_by_id('datepicker')
dt.send_keys('20/7/2011')

time.sleep(2)
#butt = driver.find_elements_by_link_text("Submit").click()
for x in self.driver.find_elements_by_link_text("Submit"):
 link = driver.ActionChains(self.driver).move_to_element(x).click(x).perform()

time.sleep(10)
driver.close()

