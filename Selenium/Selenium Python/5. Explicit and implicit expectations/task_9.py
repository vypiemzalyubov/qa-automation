from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

CONTAINER = ('xpath', '//div[@class="container"]')
RESULT = ('xpath', '//p[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 60, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.9/7/index.html')

    containers = wait.until(EC.presence_of_all_elements_located(CONTAINER))
    for i, container in enumerate(containers, start=1):
        wait.until(
            EC.element_located_to_be_selected(('xpath', f'//div[@class="container"][{i}]//input[@type="checkbox"]'))
        )
        wait.until(
            EC.element_to_be_clickable(('xpath', f'//div[@class="container"][{i}]//button[contains(text(), "Проверить")]'))
        ).click()
        result = wait.until(EC.presence_of_element_located(RESULT)).text
        if result != 'Проверьте все чекбоксы':
            print(f'Result: {result}')
