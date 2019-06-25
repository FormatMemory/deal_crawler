import argparse
import os
import sys
from config.secret import COSTCO_URL, COSTCO_DEAL_URL, COSTCO_USERNAME, COSTCO_PASSWORD
from src.crawlers.BrowserRobot import BrowserRobot
from src.crawlers.CostcoCrawler import CostcoCrawler
# import config.print_path
from config.print_path import print_path

if __name__ == '__main__':
    # print("Please choose crawler:")
    # print("1. Costco")
    # parser = argparse.ArgumentParser(description='arguments options:')
    # parser.add_argument('-c', '--crawler', type=int, default=5000, help="choose crawler.")
    # args = parser.parse_args()

    # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
    # print(COSTCO_URL, COSTCO_DEAL_URL, COSTCO_USERNAME, COSTCO_PASSWORD)
    # print_path()
    costco_crwaler = CostcoCrawler(is_dev=True)
    costco_crwaler.run()
