from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

BTN = ('xpath', '//input[@type="button"]')
INPUT = ('xpath', '//input[@id="input"]')
CHECK_BTN = ('xpath', '//input[@value="Проверить"]')
RESULT = ('xpath', '//p[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.8/2/index.html')

    button_list = wait.until(EC.presence_of_all_elements_located(BTN))
    for button in button_list:
        button.click()
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        wait.until(EC.visibility_of_element_located(INPUT)).send_keys(alert_text)
        wait.until(EC.visibility_of_element_located(CHECK_BTN)).click()

        result = wait.until(EC.presence_of_element_located(RESULT)).text
        if result != 'Неверный пин-код':
            print(f'Result: {result}')
            break
