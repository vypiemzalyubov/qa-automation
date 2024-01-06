from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/tracks")

navbar = driver.find_element("xpath", "//body/div/header/nav")
h1 = driver.find_element("xpath", '//h1[@class="mb-4"]')
card_body = driver.find_element("xpath",'(//div[@class="card-body"])[2]')
top_tracks = driver.find_element("xpath", '(//a[text()=" Top tracks "])[1]')
rounded_pill = driver.find_element("xpath", '//div[contains(@class, "mb-3")]/a[3]')
python_core = driver.find_element("xpath", '//h5[contains(text(), "Python Core")]')
footer_full_catalog = driver.find_element("xpath", '(//a[contains(@class, "btn") and text()=" Full catalog "])[2]')
