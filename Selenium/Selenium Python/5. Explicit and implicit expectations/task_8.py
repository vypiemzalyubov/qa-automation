from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

CHECKBOX = ('xpath', '//input[@type="checkbox"]')
CHECK_BTN = ('xpath', '//button[contains(text(), "Проверить")]')
RESULT = ('xpath', '//p[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 60, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.9/6/index.html')

    wait.until(EC.element_located_to_be_selected(CHECKBOX))
    wait.until(EC.element_to_be_clickable(CHECK_BTN)).click()

    result = wait.until(EC.presence_of_element_located(RESULT)).text
    print(f'Result: {result}')
