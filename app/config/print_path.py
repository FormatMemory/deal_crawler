import os

def print_path():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    CHROME_DRIVERS = os.path.join(BASE_DIR, "chromedrivers")
    print("CHROME_DRIVERS: ", CHROME_DRIVERS)