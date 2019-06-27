from config.secret import BESTBUY_API_TOKEN
from config.settings import BESTBUY_API_PRODUCTS_URL, DEBUG_MODE
import requests
import json
from src.utils.SaveSource import save_source_to_file, save_json_to_xml, save_dict_to_csv, save_list_dict_to_csv
import csv


class BestBuyCrawler:
    '''
    Fetch data via best buy api
    '''
    def __init__(self):
        pass

    def run(self, page=1):
        products = []
        for i in range(1,4):
            products.extend(self.fetch_onsale_products(page=i, percentSavings=50))
        save_list_dict_to_csv(products)

    def fetch_onsale_products(self, page=1, percentSavings=50):
        """
        Fetch onsale products via best buy api
        return a list of products
        """
        showOptions = [
                        "accessories.sku","bestSellingRank","categoryPath.id","categoryPath.name","customerReviewAverage",
                        "customerReviewCount","description","details.name","details.value","dollarSavings","features.feature",
                        "freeShipping","image","includedItemList.includedItem","longDescription","manufacturer","mobileUrl",
                        "modelNumber","name","onSale","percentSavings","regularPrice","relatedProducts.sku","salePrice",
                        "shipping","shortDescription","sku","thumbnailImage","type","upc","url"
                        ]
        params = {
            "apiKey" : BESTBUY_API_TOKEN,
            "sort" : "bestSellingRank.asc",
            "show" : ",".join(showOptions),
            "pageSize" : 100,
            "page" : page,
            "acet" : "onSale",
            "format" : "json"
        }

        special_condition = "(onSale=true&percentSavings>="+str(percentSavings)+")"
        try:
            res = requests.get(BESTBUY_API_PRODUCTS_URL+special_condition, params=params)
            res.raise_for_status()
            res.encoding = 'utf-8'

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
            print(f'Error occurred in BestBuyCrawler.fetch_onsale_products: {err}')
            return []
        else:
            print("Success")
