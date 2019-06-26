from config.secret import BESTBUY_API_TOKEN
from config.settings import BESTBUY_API_PRODUCTS_URL
import requests
from src.utils.SaveSource import save_source_to_file, save_json_to_xml

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
    def test(self):
        params = {
            "onSale": "true",
            "apiKey" : BESTBUY_API_TOKEN,
            "sort" : "bestSellingRank.asc",
            "show" : "accessories.sku,addToCartUrl,bestSellingRank,categoryPath.id,categoryPath.name,color,condition,customerReviewAverage,customerReviewCount,description,details.name,details.value,dollarSavings,features.feature,freeShipping,frequentlyPurchasedWith.sku,image,includedItemList.includedItem,inStoreAvailability,inStoreAvailabilityText,longDescription,manufacturer,mobileUrl,modelNumber,name,onlineAvailability,onlineAvailabilityText,onSale,percentSavings,regularPrice,relatedProducts.sku,salePrice,shortDescription,sku,thumbnailImage,type,upc,url",
            "pageSize" : "1",
            "acet" : "onSale",
            "format" : "json"
        }
        res = requests.get(BESTBUY_API_PRODUCTS_URL, params=params)
        print(BESTBUY_API_PRODUCTS_URL)
        print(res.status_code)
        if res.status_code == 200:
            print(res.text)
            # save_source_to_file(res.text)
            save_json_to_xml(res.text)
        else:
            print(res.text)
        