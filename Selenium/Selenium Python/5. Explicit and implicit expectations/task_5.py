from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB',
               'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 'ZM6Ms3tw',
               '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 60, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.9/3/index.html')

    for id in ids_to_find:
        wait.until(EC.visibility_of_element_located(('xpath', f'//div[@id="{id}"]'))).click()

    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    print(f'Result: {alert_text}')
