from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

ELEMENT = ('xpath', '//div[@id="block1"]')
RESULT = ('xpath', '//p[@id="message"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/draganddrop/3/index.html')

    element = wait.until(EC.visibility_of_element_located(ELEMENT))
    for i in range(1, 6):
        actions.drag_and_drop_by_offset(element, 50, 0).perform()

    result = wait.until(EC.visibility_of_element_located(RESULT)).text
    print(f'Result: {result}')
