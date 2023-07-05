import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
#
# # service = Service(executable_path='chromedriver.exe')
# # driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()

driver.get('https://quotes.toscrape.com/')

time.sleep(3)

while True:
    for div in driver.find_elements(by=By.CSS_SELECTOR, value='.quote'):
        print(div.find_element(by=By.CSS_SELECTOR, value='.text').text)
        print(div.find_element(by=By.CSS_SELECTOR, value='.author').text)
        # print(type(div.find_elements(by=By.CSS_SELECTOR, value='a.tag')))
        tags = ''
        for tag in div.find_elements(by=By.CSS_SELECTOR, value='a.tag'):
            tags += ', ' + tag.text

        print(tags.strip(', '))
    try:
        driver.find_element(by=By.CSS_SELECTOR, value='.next a').click()
    except:
        print('EXCEPTION')
        break

# print(driver.find_element(by=By.CSS_SELECTOR, value='.text'))
# print('-------------------------')
# print(type(driver.find_element(by=By.CSS_SELECTOR, value='.text')))
# print('-------------------------')
# print(driver.find_element(by=By.CSS_SELECTOR, value='.text').text)
# print('-------------------------')
# print('-------------------------')
# # print(driver.find_element(by=By.CSS_SELECTOR, value='.text'))
# print(type(driver.find_elements(by=By.CSS_SELECTOR, value='.text')))
# for tag in driver.find_elements(by=By.CSS_SELECTOR, value='.text'):
#     print(tag.text)

time.sleep(3)

driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def test_eight_components():
#     driver = webdriver.Chrome()
#
#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#
#     title = driver.title
#     assert title == "Web form"
#
#     driver.implicitly_wait(0.5)
#
#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
#
#     text_box.send_keys("Selenium")
#     submit_button.click()
#
#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"
#
#     driver.quit()
#
#
# test_eight_components()