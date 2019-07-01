from config.secret import BESTBUY_API_TOKEN
from config.settings import BESTBUY_API_PRODUCTS_URL, DEBUG_MODE
import requests
import json
from src.utils.SaveSource import save_source_to_file, save_json_to_xml, save_dict_to_csv, save_list_dict_to_csv
import csv
import time
from src.utils.Uploader import Uploader

class BestBuyCrawler:
    """
    Fetch data via best buy api
    """

    def __init__(self):
        self.defaultOptions = [
                        "accessories.sku","bestSellingRank","categoryPath.id","categoryPath.name","customerReviewAverage",
                        "customerReviewCount","description","details.name","details.value","dollarSavings","features.feature",
                        "freeShipping","includedItemList.includedItem","longDescription","manufacturer","mobileUrl",
                        "modelNumber","name","onSale","percentSavings","regularPrice","relatedProducts.sku","salePrice",
                        "shipping","shortDescription","sku","type","upc","url"
                        ]
        self.offerOptions = ["offers.endDate", "offers.startDate", "offers.text", "offers.type"]
        self.imageOptions = ["image", "accessoriesImage", "alternateViewsImage", "angleImage", "backViewImage", 
                    "energyGuideImage", "largeFrontImage", "largeImage", "leftViewImage", "mediumImage",
                "remoteControlImage","rightViewImage","spin360Url","thumbnailImage","topViewImage"]
        self.showOptions = self.defaultOptions  + self.offerOptions + self.imageOptions

        self.nomalize_dict = {
            # "image": "image",
            # "sku": "sku",
            # "date_start": "date_start",
            # "date_expire": "date_expire",
            # "details": "details",
            # "coupon_code": "coupon_code",
            # "category": "category",
            # "source": "source",
            # "features": "features",
            # "manufacturer": "manufacturer",

            "deal_link": "mobileUrl",
            "title": "name",
            "body": "longDescription",
            "customer_review": "customerReviewAverage",
            "dollar_savings": "dollarSavings",
            "model_number": "modelNumber",
            "percent_savings": "percentSavings",
            "regular_price": "regularPrice",
            "sale_price": "salePrice",
        }
    
    def run(self, totalPage=1,  *args, **kwargs):
        '''
        run BestBuy crawler,
        receive parameters: percentSavings:numeric, save_csv: boolean, upload_details:boolean
        totalPage = -1 means fetch all pages
        '''
        if "percentSavings" in kwargs:
            if kwargs["percentSavings"] < 0 or kwargs["percentSavings"] > 100:
                raise Exception("Error occured in BestBuyCrawler.run, input percentSavings should in range [0,100]")
            else:
                percentSavings = kwargs["percentSavings"]
        else:
            percentSavings = 50

        product_totalPage = self.get_total_page(percentSavings=percentSavings)
        if totalPage == -1:
            totalPage = product_totalPage
        elif totalPage > product_totalPage:
            totalPage = product_totalPage

        if "save_csv" in kwargs and kwargs["save_csv"]:
            products = []
            for i in range(1,totalPage+1):
                products.extend(self.fetch_onsale_products(page=i, percentSavings=percentSavings))
                time.sleep(1) # sleep 1 sec to avoid Over Quota
            save_list_dict_to_csv(products)

        if "upload_deals" in kwargs and kwargs["upload_deals"]:
            uploader = Uploader()
            for i in range(1,totalPage+1):
                deals = self.fetch_onsale_products(page=i, percentSavings=percentSavings)
                deals = self.normalize_deals_content(deals, self.nomalize_dict)
                uploader.upload_deals(deals)
                time.sleep(1) # sleep 1 sec to avoid Over Quota

    def normalize_deals_content(self, deals, nomalize_dict):
        """
        Normalize deal
        """
        for deal in deals:
            for k, v in nomalize_dict.items():
                if k not in deal:
                    deal[k] = deal[v]
                    del deal[v]
            if len(deal["offers"]):
                deal["date_start"] = deal["offers"][0]["startDate"]
                deal["date_expire"] = deal["offers"][0]["endDate"]
            deal["source"] = "BestBuy"
        return deals

    def fetch_onsale_products(self, page=1, percentSavings=50):
        """
        Fetch onsale products via best buy api
        return a list of products
        """

        show = ",".join(self.showOptions)
        print()
        params = {
            "apiKey" : BESTBUY_API_TOKEN,
            "sort" : "bestSellingRank.asc",
            "show" : show,
            "pageSize" : 100,
            "page" : page,
            "acet" : "onSale",
            "format" : "json"
        }

        special_condition = "(onSale=true&percentSavings>="+str(percentSavings)+")"
        try:
            res = requests.get(BESTBUY_API_PRODUCTS_URL+special_condition, params=params)
            res.raise_for_status()
            res.encoding = "utf-8"

            if DEBUG_MODE:
                # print Debug info when debug_mode is true
                for k in ["from", "to","currentPage" ,"total" ,"totalPages", "queryTime", "totalTime"]:
                    print(k+": "+ str(res.json()[k]))
                else:
                    print("")

                # # print return info in terminal
                # for i, v in enumerate(res.json()["products"]):
                #     print(i)
                #     print(v)
                #     print(".....")
                #     print(".....")

            return res.json()["products"]

        except Exception as err:
            print(f"Error occurred in BestBuyCrawler.fetch_onsale_products: {err}")
            return []
        else:
            print("Success")

    def get_total_page(self, percentSavings=50):
        """
        Fetch onsale products total pages number
        """

        show = ",".join(self.showOptions)
        params = {
            "apiKey" : BESTBUY_API_TOKEN,
            "sort" : "bestSellingRank.asc",
            "show" : show,
            "pageSize" : 100,
            "page" : 1,
            "acet" : "onSale",
            "format" : "json"
        }

        special_condition = "(onSale=true&percentSavings>="+str(percentSavings)+")"
        try:
            res = requests.get(BESTBUY_API_PRODUCTS_URL+special_condition, params=params)
            res.raise_for_status()
            res.encoding = "utf-8"
            totalPages = res.json()["totalPages"]
            time.sleep(1) # avoid Over Quota
        except Exception as err:
            print(f"Error occurred in BestBuyCrawler.get_total_page: {err}")
            return 0
        else:
            print("Total pages: "+str(totalPages ))
            return totalPages
