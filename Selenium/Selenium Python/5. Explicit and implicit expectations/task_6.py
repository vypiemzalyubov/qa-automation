from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

AD = ('xpath', '//div[@id="ad"]')
CLOSE_BTN = ('xpath', '//span[@class="close"]')
CLICK_ME_BTN = ('xpath', '//button[contains(text(), "Нажми на меня")]')
RESULT = ('xpath', '//p[@id="message"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 60, poll_frequency=1)
    driver.get('https://parsinger.ru/selenium/5.9/4/index.html')

    wait.until(EC.element_to_be_clickable(CLOSE_BTN)).click()
    wait.until(EC.invisibility_of_element_located(AD))
    wait.until(EC.element_to_be_clickable(CLICK_ME_BTN)).click()

    result = wait.until(EC.visibility_of_element_located(RESULT)).text
    print(f'Result: {result}')
