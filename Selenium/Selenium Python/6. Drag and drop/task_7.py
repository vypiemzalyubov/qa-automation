from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

BOXES = ('xpath', '//div[contains(@class, "ui-draggable")]')
RESULT = ('xpath', '//p[@id="message"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    actions = ActionChains(driver)
    driver.get('https://parsinger.ru/selenium/5.10/8/index.html')

    for box in wait.until(EC.visibility_of_any_elements_located(BOXES)):
        ids = box.get_attribute('id').split('_')[-1]
        colon = wait.until(
            EC.visibility_of_element_located(('xpath', f'//div[@id="range_{ids}"]/p'))
        )
        driver.execute_script("arguments[0].scrollIntoView();", box)
        actions.click_and_hold(box).move_to_element(colon).release().perform()

    result = wait.until(EC.visibility_of_element_located(RESULT)).text
    print(f'Result: {result}')
