from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

PIN = ('xpath', '//span[@class="pin"]')
CHECK_BTN = ('xpath', '//input[@value="Проверить"]')
RESULT = ('xpath', '//p[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.8/3/index.html')

    pin_list = wait.until(EC.visibility_of_all_elements_located(PIN))
    for pin in pin_list:
        pin_text = pin.text
        wait.until(EC.visibility_of_element_located(CHECK_BTN)).click()
        prompt = wait.until(EC.alert_is_present())
        prompt.send_keys(pin_text)
        prompt.accept()

        result = wait.until(EC.presence_of_element_located(RESULT)).text
        if result != 'Неверный пин-код':
            print(f'Result: {result}')
            break
