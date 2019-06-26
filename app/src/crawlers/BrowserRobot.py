from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from config.settings import CHROME_DRIVERS, CHROME_DRIVER_VERSIONS
import os
from src.utils.SaveSource import save_source_to_file

def get_driver(is_dev=True):
    for chrome_driver in CHROME_DRIVERS:
        if not os.path.isfile(chrome_driver):
            print("WARNING: "+ chrome_driver + " does not exist")
        else:
            try:
                chrome_options = Options()
                if not is_dev:
                    '''option to make driver work background'''
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--disable-gpu')
                driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
            except Exception as e:
                continue
            else:
                return driver
    else:
        raise Exception("ERROR: Canoot find fit Chrome driver and browser...")

class BrowserRobot:
    def __init__(self, is_dev=True):
        self.driver = get_driver(is_dev)

    def __del__(self):
        if self.driver:
            self.driver.close()
    
    def str(self):
        return str(self.driver)

    def quite_driver(self):
        if self.driver:
            self.driver.quit()

    def save_source(self, filename=""):
        assert "No results found." not in self.driver.page_source
        save_source_to_file(self.driver.page_source, filename)