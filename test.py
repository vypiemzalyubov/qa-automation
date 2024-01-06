from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/status_codes")

code_list = ["200", "301", "404", "500"]

for code in code_list:
    page = driver.find_element("xpath", f"//a[contains(text(), '{code}')]")
    page.click()
    assert code == driver.current_url[-3:], f"Invalid page. Valid page: {driver.current_url[:-3]}{code}"
    print(driver.current_url)
    driver.back()