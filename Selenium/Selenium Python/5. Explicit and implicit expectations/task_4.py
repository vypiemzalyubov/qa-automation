from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

BOX = ('xpath', '//div[@id="qQm9y1rk"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 60, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.9/2/index.html')

    wait.until(EC.presence_of_element_located(BOX)).click()

    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    print(f'Result: {alert_text}')
