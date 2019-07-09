import requests
import time
from config.settings import IMG_SAVE_PATH, DEBUG_MODE
from config.secret import DEAL_SITE_API_DOOR, DEAL_SITE_TOKEN, DEAL_SITE_API_ENDPOINT, DEAL_SITE_POST_DETAIL
from src.utils.NameGenerators import generateUniqueFileName
import json
from PIL import Image
import io


def test_upload_posts():
    headers = {
                "Authorization": "Token " + DEAL_SITE_TOKEN,
                "Content-Type": "application/x-www-form-urlencoded"
            }
    image_link = "https://img.bbystatic.com/BestBuy_US/images/products/5997/5997105_sa.jpg"
    save_file = False
    print(image_link)
    r = requests.get(image_link, stream=True, allow_redirects=True)
    r.raise_for_status()
    
    if save_file:
        if DEBUG_MODE:
            print(image_link+"\n       ---> "+save_path + name)
        with open(save_path + name, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 128):
                f.write(chunk)
        img_file = open(file_path, 'rb')
    else:
        # img_file = Image.open(io.BytesIO(r.content))
        img_file = r.content
    
    deal = {"title": "Test Image upload", "body":"image upload"}
    image = ("file.jpg", img_file)
    # deal['image'] = img_file

    print("Upload:")
    print(deal)
    # print(img_file)
    print("\n")
    
    # create post and get id
    # res = requests.post(DEAL_SITE_API_DOOR, data=deal, headers=headers)
    
    # print(res.status_code)
    # ret_json = res.json()
    # print(ret_json)
    # post_id = ret_json['id']

    # if res.status_code != 201:
    #     print(res.reason)
    #     print(res.text)
    #     raise Exception("Error orrcused at Uploader.upload_single_deal: upload error return status "+ str(res.status_code))
    # # # upload image to post
##
    post_id = 173 
    headers2 = {
        "Authorization": "Token " + DEAL_SITE_TOKEN,
        "Content-Type": "multipart/form-data"
    }
    res = requests.patch(DEAL_SITE_POST_DETAIL+str(post_id), files=img_file, headers=headers)
    if res.status_code != 200:
        print(res.reason)
        print(res.text)
        raise Exception("Error orrcused at Uploader.upload_single_deal: upload error return status "+ str(res.status_code))
    else:
        print("upload image ok")

