from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

IFRAME = ('xpath', ' //iframe')
BTN = ('xpath', '//button[@onclick="showNumber()"]')
NUMBER = ('xpath', '//p[@id="numberDisplay"]')
INPUT = ('xpath', '//input[@id="guessInput"]')
CHECK_BTN = ('xpath', '//button[@id="checkBtn"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.8/5/index.html')

    numbers = []

    iframe_list = wait.until(EC.visibility_of_all_elements_located(IFRAME))
    for iframe in iframe_list:
        driver.switch_to.frame(iframe)
        wait.until(EC.presence_of_element_located(BTN)).click()
        number = wait.until(EC.presence_of_element_located(NUMBER)).text
        numbers.append(number)
        driver.switch_to.default_content()

    for number in numbers:
        wait.until(EC.presence_of_element_located(INPUT)).send_keys(number)
        wait.until(EC.element_to_be_clickable(CHECK_BTN)).click()
        wait.until(EC.presence_of_element_located(INPUT)).clear()

        try:
            if alert := wait.until(EC.alert_is_present()):
                alert_text = alert.text
                alert.accept()
                print(f'Result: {alert_text}')
                break
        except TimeoutException:
            continue
