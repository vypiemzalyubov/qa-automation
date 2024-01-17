import os
import shutil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

folder_path = f"{os.getcwd()}\downloads"


def clear_folder(folder_path):
    shutil.rmtree(folder_path)
    os.makedirs(folder_path)


clear_folder(folder_path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1280,800")
preferences = {
    "download.default_directory": folder_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": False
}
chrome_options.add_experimental_option("prefs", preferences)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://the-internet.herokuapp.com/download")

root_div = driver.find_elements("xpath", "//div[@class='example']/a")

for i in range(1, len(root_div) + 1):
    file = driver.find_elements("xpath", "//a")[i]
    file.click()

assert len(root_div) == len(os.listdir(folder_path)), \
    f"The number of downloaded files is not equal to {len(root_div)}"
