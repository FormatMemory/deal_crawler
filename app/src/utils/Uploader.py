import requests
import time
from config.settings import IMG_SAVE_PATH, DEBUG_MODE
from config.secret import DEAL_SITE_API_DOOR, DEAL_SITE_TOKEN
from src.utils.NameGenerator import generateUniqueFileName


class Uploader:
    '''
    Upload deal to deal site 
    '''
    def __init__(self):
        ret = requests.get(DEAL_SITE_API_DOOR)
        if ret.status_code != 200:
            raise Exception("Error when initialting Uploader: Deal Site Api Door cannot be connected....", str(DEAL_SITE_API_DOOR))
        if not DEAL_SITE_TOKEN:
            raise Exception("Error when initialting Uploader: TOKEN cannot be empty...")
        self.headers = {
            "Authorization: Token ": DEAL_SITE_TOKEN
        }

    def upload_deals(self, deals, image_fields = ["image"], deal_chunk=5):
        """
        Upload deals to upload_link, there will be one second sleep for every 5 deal uploads

        """
        print("Uploader start to run...")
        count = 0
        for deal in deals:
            self.upload_single_deal(deal, image_fields, upload_link)
            count +=1
            if count%deal_chunk == 0:
                time.sleep(1)
        print("Uploader run finish")


    def upload_single_deal(self, deal, image_fields = ["image"], upload_link = DEAL_SITE_API_DOOR):
        '''
        Upload a single deal to DEALSITE
        deal: a dict contains one deal post's info.;  must contain title, body and image
        image_fields: a list of field names for image urls in input deal
        '''
        if deal is not dict:
            raise Exception("Error orrcused at Uploader.upload_single_deal: input deal should be in dict type, but "+str(type(deal))+" received")
        if "title" not in deal or "body" not in deal or "image" not in deal:
            raise Exception("Error orrcused at Uploader.upload_single_deal: input deal should at least contain title, body and image")
        
        for image_filed in image_fields:
            deal[image_filed] = image_getter(deal, image_filed)
        if DEBUG_MODE:
            print("Upload:")
            print(deal)
            print("\n")

        res = requests.post(upload_link, params=deal, headers=self.headers)
        if res.status_code != 200:
            print(res.reason)
            print(res.request)
            raise Exception("Error orrcused at Uploader.upload_single_deal: upload error")


    def image_getter(deal, image_field = "image", save_file=False, save_path=IMG_SAVE_PATH):
        '''
        Get Image file from link deal[image_field]
        Save file to SAVE_PATH
        '''
        url = deal[image_field]
        filetype = url.replace(' ', '').split('.')[-1]
        if "source" in deal:
            name = generateUniqueFileName(filetype, deal["source"])
        else:
            name = generateUniqueFileName(filetype, "")
        r = requests.get(url, stream=True, allow_redirects=True)
        r.raise_for_status()
        if save_file:
            if DEBUG_MODE:
                print(url+"\n       ---> "+save_path + name)
            with open(save_path + name, 'wb') as f:
                for chunk in r.iter_content(chunk_size = 128):
                    f.write(chunk)
        return r.content