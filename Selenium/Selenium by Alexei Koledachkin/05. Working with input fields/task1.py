from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

TEST_NAME = "John Malkovich"
TEST_EMAIL = "test@mail.com"
TEST_CURRENT_ADDRESS = "Route E-95"
TEST_PERMANENT_ADDRESS = "Earth"

full_name = driver.find_element("xpath", "//input[@id='userName']")
full_name.clear()
assert full_name.get_attribute("value") == ""
full_name.send_keys(TEST_NAME)
assert TEST_NAME == full_name.get_attribute("value"), \
    f"Invalid Full Name. Valid: {TEST_NAME}"

email = driver.find_element("xpath", "//input[@id='userEmail']")
email.clear()
assert email.get_attribute("value") == ""
email.send_keys(TEST_EMAIL)
assert TEST_EMAIL == email.get_attribute("value"), \
    f"Invalid Email. Valid: {TEST_EMAIL}"

current_address = driver.find_element("xpath", "//textarea[@id='currentAddress']")
current_address.clear()
assert current_address.get_attribute("value") == ""
current_address.send_keys(TEST_CURRENT_ADDRESS)
assert TEST_CURRENT_ADDRESS == current_address.get_attribute("value"), \
    f"Invalid Current Address. Valid: {TEST_CURRENT_ADDRESS}"

permanent_address = driver.find_element("xpath", "//textarea[@id='permanentAddress']")
permanent_address.clear()
assert permanent_address.get_attribute("value") == ""
permanent_address.send_keys(TEST_PERMANENT_ADDRESS)
assert TEST_PERMANENT_ADDRESS == permanent_address.get_attribute("value"), \
    f"Invalid Permanent Address. Valid: {TEST_PERMANENT_ADDRESS}"