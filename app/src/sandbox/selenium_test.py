from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "../chromedrivers/chromedriver"
versions = ["76", "75", "74", "73"]

print("Start...")
for version in versions:
    try:
        driver = webdriver.Chrome(CHROME_DRIVER_PATH+"_"+version)
    except Exception as e:
        continue
    else:
        break
else:
    raise("ERROR: Canoot find fit Chrome driver and browser...")
# version = driver.capabilities['version']
print("Chrome version: "+version)
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
