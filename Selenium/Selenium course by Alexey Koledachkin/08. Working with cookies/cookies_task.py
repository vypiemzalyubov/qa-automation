import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Selenium")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

AMAZON_URL = "https://www.amazon.com/"
MVIDEO_URL = "https://www.mvideo.ru/products/noutbuk-igrovoi-thunderobot-911-m-g3-pro-400135845"
ADD_TO_CART_BUTTON = ("xpath", "//button[@title='Добавить в корзину']")
GO_TO_CART_BUTTON = ("xpath", "//button[@title='Перейти в корзину']")


print("Start test: Setting and reading cookies")

driver.get(AMAZON_URL)

driver.add_cookie({
    "name": "username",
    "value": "user123"
})

driver.refresh()

assert driver.get_cookie("username")["name"] == "username", \
    "No cookie named \"username\""

assert driver.get_cookie("username")["value"] == "user123", \
    "No cookie with the value of \"user123\""

print(f'"username" cookie: {driver.get_cookie("username")}')

print("Finish test: Setting and reading cookies")


print("Start test: Deleting cookies")

driver.get(AMAZON_URL)

all_cookies_before = driver.get_cookies()
all_cookie_names_before = [cookie["name"] for cookie in all_cookies_before]
driver.delete_cookie(all_cookie_names_before[0])
all_cookies_after = driver.get_cookies()
all_cookie_names_after = [cookie["name"] for cookie in all_cookies_after]

assert all_cookie_names_before[0] not in all_cookie_names_after, \
    f"The \"{all_cookie_names_before[0]}\" cookie is there, but it shouldn't be"

print("Finish test: Deleting cookies")


print("Start test: Shopping cart automation")

driver.get(MVIDEO_URL)

wait.until(EC.element_to_be_clickable(ADD_TO_CART_BUTTON)).click()
wait.until(EC.element_to_be_clickable(GO_TO_CART_BUTTON))

pickle.dump(driver.get_cookies(), open(f"{os.getcwd()}/cookies/cookies.pkl", "wb"))

driver.delete_all_cookies()
driver.refresh()

wait.until(EC.invisibility_of_element_located(GO_TO_CART_BUTTON))

cookies = pickle.load(open(f"{os.getcwd()}/cookies/cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()

wait.until(EC.element_to_be_clickable(GO_TO_CART_BUTTON))

print("Finish test: Shopping cart automation")
