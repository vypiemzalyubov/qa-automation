from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-cache')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

RESULT = ('xpath', '//span[@id="result"]')

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 15, poll_frequency=1)
    driver.get('https://parsinger.ru/window_size/2/index.html')

    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

    for x in window_size_x:
        for y in window_size_y:
            driver.set_window_size(x, y)

            result = wait.until(EC.presence_of_element_located(RESULT)).text
            if result:
                print(
                    f"Result: {{'width': {driver.execute_script('return window.innerWidth;')}, 'height': {driver.execute_script('return window.innerHeight;')}}}"
                )
                break
