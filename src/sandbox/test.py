import requests
from requests.exceptions import HTTPError

url = "https://www.costco.com"#/LogonForm"
url = "http://google.com"
print("start")
try:
    res = requests.get(url, timeout=1000)
    res.raise_for_status()
# requests.post(url, )
except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
except Exception as err:
        print(f'Other error occurred: {err}')
else:
    print("success")
    print(res)
    print(res.status_code)
    res.encoding = "UTF-8"
    # print(res.text)
    
finally:
    print("end")

def login(url, username, password):
    '''
    Simulate login via username and password
    '''
    payload = {
        'username': username,
        'password': password
    }

    try:
        res = requests.post(
            url,
            data=payload
        )
    except HTTPError as http_err:
        print(f'Login error, HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Login error, Other error occurred: {err}')
    except Exception as e:
        raise e
    else:
        print("Login Sucess")
        return res

login_url = "http://pythonscraping.com/pages/cookies/welcome.php"
res = login(login_url, "david", "password")
res.encoding = "UTF-8"
print(res.text)
print(res.cookies.get_dict())
r = requests.get(
    "http://pythonscraping.com/pages/cookies/profile.php",
    cookies=res.cookies
)
# print(r.text)

payload = {
    'username': 'dadawa',
    'password': 'password'
}
session = requests.Session()
r2 = session.post(login_url, data=payload)
print(r2.cookies.get_dict())
r2 = session.get(
    "http://pythonscraping.com/pages/cookies/profile.php",
    )
print(r2.text)
