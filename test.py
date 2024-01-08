import os
import time
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Selenium")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

BASE_URL = "https://www.amazon.com/"

driver.get(BASE_URL)

print("Start test: Setting and reading cookies")
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
all_cookies_before = driver.get_cookies()
all_cookie_names_before = [cookie["name"] for cookie in all_cookies_before]
driver.delete_cookie(all_cookie_names_before[0])
all_cookies_after = driver.get_cookies()
all_cookie_names_after = [cookie["name"] for cookie in all_cookies_after]
assert all_cookie_names_before[0] not in all_cookie_names_after, \
    f"The \"{all_cookie_names_before[0]}\" cookie is there, but it shouldn't be"
print("Finish test: Deleting cookies")
