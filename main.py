import time

from selenium import webdriver
driver = webdriver.Chrome()
def momazosdiego():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('file:///Users/scarlatdorianandrei/PycharmProjects/sigma/diego.mp4')
    time.sleep(13)
    driver.quit()

def momazospablo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("file:///Users/scarlatdorianandrei/PycharmProjects/sigma/momazos%20pablo.mp4")
    driver.maximize_window()
    time.sleep(6.5)
    driver.quit()

def momazosluis():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("file:///Users/scarlatdorianandrei/PycharmProjects/sigma/Momazos%20Luis.mp4")
    time.sleep(7)
    driver.quit()

def momazosjuan():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("file:///Users/scarlatdorianandrei/PycharmProjects/sigma/momazos%20Jua.mp4")
    time.sleep(15)
    driver.quit()



momazosdiego()
momazospablo()
momazosluis()
momazosjuan()