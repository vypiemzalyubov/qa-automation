from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

BTN = ('xpath', '//input[@type="button"]')
RESULT = ('xpath', '//p[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.8/1/index.html')

    button_list = wait.until(EC.presence_of_all_elements_located(BTN))
    for button in button_list:
        button.click()
        wait.until(EC.alert_is_present()).accept()

        result = wait.until(EC.presence_of_element_located(RESULT)).text
        if result:
            print(f'Result: {result}')
            break
