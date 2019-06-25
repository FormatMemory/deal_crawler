import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.costco.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

headers2 = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

data = {
    "logonId": "@gmail.com",
    "logonPassword": "",
    "option1": "on",
    "reLogonURL": "LogonForm",
    "isPharmacy": "false",
    "fromCheckout":"",
    "authToken": "-1002%2C5M9R2fZEDWOZ1d8MBwy40LOFIV0%3D",
    "URL": "Lw=="
}
data2 = {
    "logonId": "%40gmail.com",
    "logonPassword": "",
    "option1": "on",
    "reLogonURL": "LogonForm",
    "isPharmacy": "false",
    "fromCheckout":"",
    "authToken": "-1002%252C5M9R2fZEDWOZ1d8MBwy40LOFIV0%253D",
    "URL": "Lw%3D%3D"
}
header = {
    "authority": "www.costco.com",
    "path": "/Logon",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.costco.com",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

payload = {
    "logonId": "@gmail.com",
    "logonPassword": "",
    "option1": "on",
    "reLogonURL": "LogonForm",
    "isPharmacy": "false",
    "fromCheckout":"",
    "authToken": "-1002%2C5M9R2fZEDWOZ1d8MBwy40LOFIV0%3D",
    "URL": "Lw=="
}

try:
    with open(cookies) as f:
        j = json.load(f)
    response = session.post(URL, timeout=2, headers=header, data=payload)
    # response = session.get(URL, timeout=2, headers=headers)
    if response.status_code == 200:
        # success
        print("success")
        # print(response.text)

        # # write to a response.text to a file 
        # with open("./a.html", 'w') as f:
        #     f.write(response.text)
        print(response.cookies)
        # print(response.content)
        session.cookies = j
        res = session.get("https://www.costco.com/LG-30CuFt-4-Door-French-Door-InstaView-Refrigerator-with-Door-in-Door.product.100339491.html", timeout=2, headers=header, cookies=session.cookies)
        with open("./tmp/b.html", 'w') as f:
            f.write(res.text)
        print(res.text)
    else:
        print("faild")
except requests.ConnectionError as e:
    print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
    print(str(e))
except requests.Timeout as e:
    print("OOPS!! Timeout Error")
    print(str(e))
except requests.RequestException as e:
    print("OOPS!! General Error")
    print(str(e))
except KeyboardInterrupt:
    print("Someone closed the program")

# html = requests.get(URL).text
# soup = BeautifulSoup(html, "lxml")
# img_ul = soup.find_all("li", {"class", "poster"})


