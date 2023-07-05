import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.deepl.com/ru/translator')

close_cookie = driver.find_element(by=By.CSS_SELECTOR, value='button.dl_cookieBanner--buttonClose')

time.sleep(2)

close_cookie.click()

time.sleep(8)

language_selector_btn = driver.find_element(by=By.CSS_SELECTOR,
                                            value='[data-testid="translator-target-lang"]'
                                            )

time.sleep(5)

language_selector_btn.click()

time.sleep(2)

driver.quit()