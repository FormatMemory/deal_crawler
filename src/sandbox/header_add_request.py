import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.costco.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

try:
    response = requests.get(URL, timeout=3, headers=headers)
    if response.status_code == 200:
        # success
        print("success")
        print(response.text)
    else:
        print("faid")
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


