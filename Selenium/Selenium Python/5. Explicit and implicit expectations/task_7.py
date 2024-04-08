from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

BOX = ('xpath', '//div[@class="box_button"]')
CLOSE_BTN = ('xpath', '//button[@id="close_ad"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 60, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.9/5/index.html')

    result = []

    boxes = wait.until(EC.visibility_of_all_elements_located(BOX))
    for box in boxes:
        box.click()
        wait.until(EC.element_to_be_clickable(CLOSE_BTN)).click()
        wait.until(EC.invisibility_of_element_located(CLOSE_BTN))
        wait.until(lambda _: box.text != '')
        result.append(box.text)

    result = '-'.join(result)
    print(f'Result: {result}')
