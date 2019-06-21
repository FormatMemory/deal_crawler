import requests
from bs4 import BeautifulSoup
import os
import re

URL = "https://www.costco.com"

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
def parseCookieFile(cookiefile):
    """Parse a cookies.txt file and return a dictionary of key value pairs
    compatible with requests."""

    cookies = {}
    with open (cookiefile, 'r') as fp:
        for line in fp:
            if not re.match(r'^\#', line):
                lineFields = line.strip().split('\t')
                cookies[lineFields[5]] = lineFields[6]
    return cookies

cookies = parseCookieFile('./tmp/cookies.txt')
print(cookies)
res = requests.get("https://www.costco.com/LG-30CuFt-4-Door-French-Door-InstaView-Refrigerator-with-Door-in-Door.product.100339491.html",
            timeout=2, 
            headers=header, cookies=cookies)
with open("./tmp/c.html", 'w') as f:
    f.write(res.text)
print(res.text)

# html = requests.get(URL).text
# soup = BeautifulSoup(html, "lxml")
# img_ul = soup.find_all("li", {"class", "poster"})


