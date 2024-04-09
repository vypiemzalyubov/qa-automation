from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

RED = ('xpath', '//div[@id="draggable"]')
GRAY = ('xpath', '//div[@class="box"]')
RESULT = ('xpath', '//div[@id="message"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/draganddrop/2/index.html')

    gray_boxes = wait.until(EC.visibility_of_any_elements_located(GRAY))
    for i, box in enumerate(gray_boxes, start=1):
        element = wait.until(EC.visibility_of_element_located(RED))
        target = wait.until(EC.visibility_of_element_located(('xpath', f'//div[@id="box{i}"]')))
        actions.drag_and_drop(element, target).perform()

    result = wait.until(EC.visibility_of_element_located(RESULT)).text
    print(f'Result: {result}')
