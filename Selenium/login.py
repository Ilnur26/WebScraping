import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')
time.sleep(2)

driver.find_element(by=By.CSS_SELECTOR, value='.header-box p a').click()

time.sleep(2)

username = driver.find_element(by=By.CSS_SELECTOR, value='#username')
pswd = driver.find_element(by=By.CSS_SELECTOR, value='#password')
submit_btn = driver.find_element(by=By.CSS_SELECTOR, value='.btn')
username.send_keys('login1')
pswd.send_keys('qwerty')

time.sleep(2)

submit_btn.click()

time.sleep(2)

driver.quit()
