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

    def run(self):
        params = {
            "apiKey" : BESTBUY_API_TOKEN,
            "sort" : "bestSellingRank.asc",
            "show" : "accessories.sku,bestSellingRank,categoryPath.id,categoryPath.name,customerReviewAverage,customerReviewCount,description,details.name,details.value,dollarSavings,features.feature,freeShipping,image,includedItemList.includedItem,longDescription,manufacturer,mobileUrl,modelNumber,name,onSale,percentSavings,regularPrice,relatedProducts.sku,salePrice,shipping,shortDescription,sku,thumbnailImage,type,upc,url",
            "pageSize" : 3,
            "page" : 2,
            "acet" : "onSale",
            "format" : "json"
        }
        special_condition = "(onSale=true&percentSavings>50)"
        try:
            res = requests.get(BESTBUY_API_PRODUCTS_URL+special_condition, params=params, timeout=3)
            res.raise_for_status()
            res.encoding = 'utf-8'

            if DEBUG_MODE:
                # print Debug info when debug_mode is true
                for k in ["from", "to","currentPage" ,"total" ,"totalPages", "queryTime", "totalTime"]:
                    print(k+": "+ str(res.json()[k]))
                else:
                    print("")
            source = res.json()["products"]
            for p in res.json()["products"]:
                print(p)
                print(".....")
                print(".....")
            save_list_dict_to_csv(source)
           
        except Exception as err:
            print(f'Error occurred: {err}')
        else:
            print("Success")
