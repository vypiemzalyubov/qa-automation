import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1280,800")
chrome_options.add_argument("--ignore-certificate-errors")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

BASE_URL = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"
CHANGE_TEXT_BUTTON = ("xpath", "//button[@id='populate-text']")
TEXT_AFTER_CLICK = ("xpath", "//h2[@id='h2']")
DISPLAY_AFTER_10_SECONDS_BUTTON = ("xpath", "//button[@id='display-other-button']")
HIDDEN_BUTTON = ("xpath", "//button[@id='hidden']")
ENABLE_AFTER_10_SECONDS_BUTTON = ("xpath", "//button[@id='enable-button']")
DISABLE_BUTTON = ("xpath", "//button[@id='disable']")

driver.get(BASE_URL)

print("Start test: Click on the \"Change Text to Selenium Webdriver\" button and wait for the element text to change next to it")
click_change_button = driver.find_element(*CHANGE_TEXT_BUTTON)
click_change_button.click()
wait.until(EC.text_to_be_present_in_element(TEXT_AFTER_CLICK, "Selenium Webdriver"))
new_text = wait.until(EC.visibility_of_element_located(TEXT_AFTER_CLICK)).text
assert new_text == "Selenium Webdriver", \
    f"Invalid text in field: {new_text}. Valid: Selenium Webdriver"
print("Finish test: Click on the \"Change Text to Selenium Webdriver\" button and wait for the element text to change next to it")


print("Start test: Click on the \"Display button after 10 seconds\" and wait for the \"Enabled\" button to appear")
click_display_button = driver.find_element(*DISPLAY_AFTER_10_SECONDS_BUTTON)
click_display_button.click()
enabled_text = wait.until(EC.visibility_of_element_located(HIDDEN_BUTTON)).text
assert enabled_text == "Enabled", \
    f"Invalid text in button: {enabled_text}. Valid: Enabled"
print("Finish test: Click on the \"Display button after 10 seconds\" and wait for the \"Enabled\" button to appear")

print("Start test: Click on the \"Enable button after 10 seconds\" button and wait for the \"Button\" button to be clickable")
click_enable_button = driver.find_element(*ENABLE_AFTER_10_SECONDS_BUTTON)
click_enable_button.click()
disable_button = wait.until(EC.element_to_be_clickable(DISABLE_BUTTON))
assert isinstance(disable_button, selenium.webdriver.remote.webelement.WebElement), \
    f"Invalid object type: {type(disable_button)}"
print("Finish test: Click on the \"Enable button after 10 seconds\" button and wait for the \"Button\" button to be clickable")
