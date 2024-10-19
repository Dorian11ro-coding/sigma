import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://momazosdiego.com/momazo.mp4')
time.sleep(500000)