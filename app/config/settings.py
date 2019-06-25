# secret info
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME_DRIVER_PATH = os.path.join(BASE_DIR, "chromedrivers")
CHROME_DRIVER_VERSIONS = ["1221","76", "75", "74", "73"]
CHROME_DRIVERS = [
    os.path.join(CHROME_DRIVER_PATH, "chromedriver_" + dv) for dv in CHROME_DRIVER_VERSIONS
]
OUTPUT_FILE_PATH =  os.path.join(BASE_DIR, "output")