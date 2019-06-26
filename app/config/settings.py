# secret info
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME_DRIVER_PATH = os.path.join(BASE_DIR, "chromedrivers")
CHROME_DRIVER_VERSIONS = ["76", "75", "74", "73"]
CHROME_DRIVERS = [
    os.path.join(CHROME_DRIVER_PATH, "chromedriver_" + dv) for dv in CHROME_DRIVER_VERSIONS
]
OUTPUT_FILE_PATH =  os.path.join(BASE_DIR, "output")

COSTCO_URL = "https://www.costco.com/"
COSTCO_DEAL_URL = "https://www.costco.com/warehouse-hot-buys.html"

BESTBUY_DEAL_URL = ""
BESTBUY_API_URL = "http://api.bestbuy.com/v1/"
BESTBUY_API_PRODUCTS_URL = "https://api.bestbuy.com/v1/products"