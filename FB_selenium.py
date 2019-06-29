# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 15:30:05 2019

@author: khushal
"""
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

'''

### Login to Syntel portal automatically
user = "KS5046082"
pwd = "#####"
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(chrome_options=chrome_options)

#driver.get("http://www.facebook.com")
driver.maximize_window()
driver.get("https://www.myatos-syntel.net")

assert "Login" in driver.title

elem = driver.find_element_by_id("_com_liferay_login_web_portlet_LoginPortlet_kpoUserName")
elem.send_keys(user)
elem = driver.find_element_by_id("_com_liferay_login_web_portlet_LoginPortlet_kpoPassword")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 15)

elem_my_image = driver.find_element_by_id("T")
actions=ActionChains(driver)
actions.click(elem_my_image)
actions.perform

print("driver.current_url = ",driver.current_url)

driver.close()
'''


user = "khushalsawant2010@gmail.com"
pwd = "xxxxxxxx"

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(chrome_options=chrome_options)

#driver.get("http://www.facebook.com")
driver.maximize_window()
driver.get("https://www.naukri.com/nlogin/login")

actions=ActionChains(driver)

#assert "Login" in driver.title

elem = driver.find_element_by_id("usernameField")
elem.send_keys(user)
elem = driver.find_element_by_id("passwordField")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

time.sleep(15)

wait = WebDriverWait(driver, 20)

elem_home_profile = driver.find_element_by_xpath("//*[@id='root']/div/div/span/div/div/div/div[2]/div/div[2]/div[1]/div/a[1]/div[2]")
actions.click(elem_home_profile)
actions.perform()
file_path="C:/Users/khushal/Documents/Python-Khushal Sawant with 5+ exp. Resume.pdf"
elem_attach_CV = driver.find_element_by_xpath("//*[@id='attachCV']").send_keys(file_path)
actions.click(elem_attach_CV)
actions.perform()
#elem_my_image = driver.find_element_by_id("T")

print("driver.current_url = ",driver.current_url)

#driver.close()