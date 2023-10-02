#print(details['username'],details['password'])
from check import details
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import time


driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.linkedin.com/')
time.sleep(1)
driver.find_element(by=By.XPATH,value='//*[@id="session_key"]').send_keys(details['username'])
driver.find_element(by=By.XPATH,value='//*[@id="session_password"]').send_keys(details['password'])
driver.find_element(by=By.XPATH,value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()
time.sleep(1)
driver.find_element(by=By.XPATH,value='//*[@id="global-nav-typeahead"]/input').send_keys('iim')
driver.find_element(by=By.XPATH,value='//*[@id="global-nav-typeahead"]/input').send_keys(Keys.ENTER)
time.sleep(3)

