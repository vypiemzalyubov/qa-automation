from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

GREEN = ('xpath', '//div[contains(@class, "ui-draggable-handle")]')
GRAY = ('xpath', '//div[@class="draganddrop_end"]')
RESULT = ('xpath', '//p[@id="message"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/selenium/5.10/2/index.html')

    green_boxes = wait.until(EC.visibility_of_any_elements_located(GREEN))
    for i, box in enumerate(green_boxes, start=1):
        element = wait.until(EC.visibility_of_element_located(('xpath', f'//div[@id="draganddrop{i}"]')))
        target = wait.until(EC.visibility_of_element_located(GRAY))
        actions.drag_and_drop(element, target).perform()

    result = wait.until(EC.visibility_of_element_located(RESULT)).text
    print(f'Result: {result}')
