from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

BASE_URL = 'https://parsinger.ru/selenium/1/1.html'
INPUT_FIELD = ('xpath', '//input[@type="text"]')
SUBMIT_BTN = ('xpath', '//input[@value="Отправить"]')
RESULT = ('xpath', '//input[@value="Отправить"]/following-sibling::*')

driver.get(BASE_URL)

fields = wait.until(EC.visibility_of_all_elements_located(INPUT_FIELD))

for field in fields:
    field.send_keys('Текст')

wait.until(EC.element_to_be_clickable(SUBMIT_BTN)).click()
result = wait.until(EC.visibility_of_element_located(RESULT)).text
print(f'Result: {result}')
