import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

HEX_SPAN = ('xpath', '//span')
CHECK_ALL = ('xpath', '//button[contains(text(), "Проверить все элементы")]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.5/5/1.html')

    hex_list = wait.until(EC.visibility_of_all_elements_located(HEX_SPAN))
    for i, hex in enumerate(hex_list, start=1):
        hex_value = hex.text
        select = Select(
            wait.until(EC.presence_of_element_located(('xpath', f'//div[contains(@style, "background")][{i}]//select')))
        )
        select.select_by_value(hex_value)

        wait.until(
            EC.element_to_be_clickable(
                ('xpath', f'//div[contains(@style, "background")][{i}]//button[@data-hex="{hex_value}"]')
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                ('xpath', f'//div[contains(@style, "background")][{i}]//input[@type="checkbox"]')
            )
        ).click()

        wait.until(
            EC.visibility_of_element_located(
                ('xpath', f'//div[contains(@style, "background")][{i}]//input[@type="text"]')
            )
        ).send_keys(hex_value)

        wait.until(
            EC.element_to_be_clickable(
                ('xpath', f'//div[contains(@style, "background")][{i}]//button[contains(text(), "Проверить")]')
            )
        ).click()

    wait.until(EC.element_to_be_clickable(CHECK_ALL)).click()
    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    print(f'Result: {alert_text}')        
