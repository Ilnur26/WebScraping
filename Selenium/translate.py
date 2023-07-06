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

btn_turk = driver.find_element(by=By.CSS_SELECTOR, value='button[data-testid="translator-lang-option-tr"]')

time.sleep(2)

btn_turk.click()

time.sleep(2)

inputText = driver.find_element(by=By.CSS_SELECTOR, value='div[_d-id="1"]')

time.sleep(2)

inputText.send_keys('''Все счастливые семьи похожи друг на друга,
каждая несчастливая семья несчастлива по-своему.
Все смешалось в доме Облонских.
Жена узнала, что муж был в связи с бывшею в их доме француженкою-гувернанткой,
и объявила мужу, что не может жить с ним в одном доме''')

# inputText.send_keys('''Перевод''')

time.sleep(5)

res = ''

outputTranslation = driver.find_elements(by=By.CSS_SELECTOR, value='div[aria-labelledby="translation-results-heading"] span')

time.sleep(2)
i = 1
# print(outputTranslation)
for tr in outputTranslation:
    # print(i)
    # print(tr.text)
    # i+=1
    res += tr.text + ' '

# print(res)

with open('translation.txt', 'w', encoding='utf-8') as f:
    f.write(res)

driver.quit()