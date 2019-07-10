import argparse
import os
import sys
from src.crawlers.BrowserRobot import BrowserRobot
from src.crawlers.CostcoCrawler import CostcoCrawler
from config.print_path import print_path
from src.crawlers.BestBuyCrawler.BestBuyCrawler import BestBuyCrawler

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='arguments options:')
    # parser.add_argument('-c', '--crawler', type=int, default=5000, help="choose crawler.")
    # args = parser.parse_args()

    # print_path()


    # costco_crwaler = CostcoCrawler(is_dev=False)
    # costco_crwaler.run()
    
    bb = BestBuyCrawler()
    bb.run(totalPage = 4, percentSavings=75, save_csv=False, upload_deals=True)

    # from src.sandbox.uploadImage import test_upload_posts_together
    # test_upload_posts_together()

