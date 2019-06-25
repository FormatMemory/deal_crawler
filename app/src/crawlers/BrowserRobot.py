from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config.settings import CHROME_DRIVERS, CHROME_DRIVER_VERSIONS, OUTPUT_FILE_PATH
import os
import datetime

def get_driver():
    for chrome_driver in CHROME_DRIVERS:
        if not os.path.isfile(chrome_driver):
            print("WARNING: "+ chrome_driver + " does not exist")
        else:
            try:
                driver = webdriver.Chrome(chrome_driver)
            except Exception as e:
                continue
            else:
                return driver
    else:
        raise Exception("ERROR: Canoot find fit Chrome driver and browser...")

class BrowserRobot:
    def __init__(self):
        self.driver = get_driver()

    def __del__(self):
        if self.driver:
            self.driver.close()
    
    def str(self):
        return str(self.driver)

    def quite_driver(self):
        if self.driver:
            self.driver.quit()

    def save_source(self, filename=""):
        if not filename:
            filename = 'test-{date:%Y-%m-%d_%H:%M:%S}.html'.format( date=datetime.datetime.now() )
        path = os.path.join(OUTPUT_FILE_PATH, filename)
        html = self.driver.page_source
        with open(path, 'w') as f:
            f.write(html)
        assert "No results found." not in self.driver.page_source
        print("Save file at "+path)