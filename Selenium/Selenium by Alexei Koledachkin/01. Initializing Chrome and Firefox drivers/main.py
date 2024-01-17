# Chrome first method

from selenium import webdriver

driver = webdriver.Chrome()

# Chrome second method

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Firefox first method

from selenium import webdriver

driver = webdriver.Firefox()

# Firefox second method

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Firefox second method (Ubuntu)

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service("/snap/bin/geckodriver")
driver = webdriver.Firefox(service=service)