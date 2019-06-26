from config.secret import BESTBUY_API_TOKEN
from config.settings import BESTBUY_API_PRODUCTS_URL
import requests
import json
from src.utils.SaveSource import save_source_to_file, save_json_to_xml, save_json_to_csv

class BestBuyCrawler:
    '''
    Fetch data via best buy api
    '''
    def __init__(self):
        pass
# https://api.bestbuy.com/v1/products(onSale=true)?apiKey=t33gXz67AmsMunsbHwNWFXDI
# &sort=bestSellingRank.asc
# &show=accessories.sku,addToCartUrl,bestSellingRank,categoryPath.id,categoryPath.name,color,condition,customerReviewAverage,customerReviewCount,description,details.name,details.value,dollarSavings,features.feature,freeShipping,frequentlyPurchasedWith.sku,image,includedItemList.includedItem,inStoreAvailability,inStoreAvailabilityText,longDescription,manufacturer,mobileUrl,modelNumber,name,onlineAvailability,onlineAvailabilityText,onSale,percentSavings,regularPrice,relatedProducts.sku,salePrice,shortDescription,sku,thumbnailImage,type,upc,url
# &facet=onSale
# &pageSize=14
# &format=json
    def run(self):
        params = {
            "apiKey" : BESTBUY_API_TOKEN,
            "sort" : "bestSellingRank.asc",
            "show" : "accessories.sku,bestSellingRank,categoryPath.id,categoryPath.name,customerReviewAverage,customerReviewCount,description,details.name,details.value,dollarSavings,features.feature,freeShipping,image,includedItemList.includedItem,longDescription,manufacturer,mobileUrl,modelNumber,name,onSale,percentSavings,regularPrice,relatedProducts.sku,salePrice,shipping,shortDescription,sku,thumbnailImage,type,upc,url",
            "pageSize" : "3",
            "page" : "1",
            "acet" : "onSale",
            "format" : "json"
        }
        special_condition = "(onSale=true&percentSavings>50)"
        try:
            res = requests.get(BESTBUY_API_PRODUCTS_URL+special_condition, params=params, timeout=3)
            res.raise_for_status()
            res.encoding = 'utf-8'
            # print(res.text)
            # save_source_to_file(res.text)
            # save_json_to_xml(res.json()["products"])
            # print(res.json()["products"])
            # save_json_to_csv(json.loads(res.json()["products"]))
            source = res.json()["product"]
            print(type(source))
        except Exception as err:
            print(f'Error occurred: {err}')
        else:
            print("Success")
        