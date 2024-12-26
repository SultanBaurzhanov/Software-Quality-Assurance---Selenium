from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get('https://practicetestautomation.com/practice-test-login/')

name = driver.find_element(By.ID, 'username')
name.send_keys("student")

password = driver.find_element(By.ID, 'password') 
password.send_keys("Password123")

submit = driver.find_element(By.ID, 'submit')
submit.send_keys(Keys.ENTER)

logout = driver.find_element(By.LINK_TEXT, 'Log out')
logout.send_keys(Keys.ENTER)

breakpoint()