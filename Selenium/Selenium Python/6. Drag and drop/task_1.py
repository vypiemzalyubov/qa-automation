from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

ELEMENT = ('xpath', '//div[@id="draggable"]')
TARGET = ('xpath', '//div[@id="field2"]')
RESULT = ('xpath', '//div[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/draganddrop/1/index.html')

    element = wait.until(EC.visibility_of_element_located(ELEMENT))
    target = wait.until(EC.visibility_of_element_located(TARGET))
    actions.drag_and_drop(element, target).perform()

    result = wait.until(EC.presence_of_element_located(RESULT)).text
    print(f'Result: {result}')
