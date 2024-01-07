import os
import shutil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1280,800")
preferences = {
    "download.default_directory": f"{os.getcwd()}\downloads",
    "download.prompt_for_download": False, 
    "download.directory_upgrade": True,
    "safebrowsing.enabled": False 
}
chrome_options.add_experimental_option("prefs", preferences)
# chrome_options.page_load_strategy = 'eager'
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--disable-cache")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

folder_path = f"{os.getcwd()}\downloads"

def clear_folder(folder_path): 
    shutil.rmtree(folder_path) 
    os.makedirs(folder_path)
clear_folder(folder_path)

driver.get("https://the-internet.herokuapp.com/download")

time.sleep(3)
driver.find_elements("xpath", "//a")[3].click()
time.sleep(3)


# driver.get("https://the-internet.herokuapp.com/upload")
# upload = driver.find_element("xpath", "//input[@type='file']").send_keys(f"{os.getcwd()}\downloads\Test1.pdf")
# print(f"{os.getcwd()}\downloads")