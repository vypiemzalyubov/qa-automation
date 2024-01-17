from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

wiki_icon = driver.find_element("class name", "wikipedia-icon")
wiki_input_by_id = driver.find_element("id", "Wikipedia1_wikipedia-search-input")
wiki_input_by_class = driver.find_element("class name", "wikipedia-search-input")
h2_elem = driver.find_element("tag name", "h2")