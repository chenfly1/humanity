import requests

# 请求的 URL
url = "https://testnet.humanity.org/api/claim/referralRewards"

# 请求头
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "authorization": "",
    "content-length": "0",
    "cookie": "AjBOmW2JBjgDyPz35D7/YciYN7KErx60xzerWuXAHOvIvRWOghrnXa7NEzmOHtMqH9T3ZEC/Pb6sg72CHVIgMYJ6WLbRq9xPkv4BXWeiRA+QTBtiqzAFhuEcdpY224ewXc47roBiDRh8rljollB5VDL5BfZeRcrLtawwF0PGTbPetvCVMgA3w6do3d2VAiTq3Czd10Pj7yr2WAfk4kUf0lfbupmNkUnevNh6vlmp9Y8swK3x/QyB8nye/DkVTdvC",
    "origin": "https://testnet.humanity.org",
    "priority": "u=1, i",
    "referer": "https://testnet.humanity.org/dashboard",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "token": "AjBOmW2JBjgDyPz35D7/YciYN7KErx60xzerWuXAHOvIvRWOghrnXa7NEzmOHtMqQfJA0hczuvlndyR7R41QQtTxENuZcp8pMFZ6AlW+rZcJE6XO+RfQVNjs6QDCdAq4bOPUQLVOJMGn4Bk2ZykBqU7i5ZU8Hvi37cBIhAso8pjdhZTTp7BuDA6zZmjK35VHpYAltZh3wEGlk5Ixp8QxbBCqJpUBObixd1wmueeF4si/6KchqVSt/pP600QdacU8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}

# 发送 POST 请求
response = requests.post(url,headers=headers,timeout=30)

# 输出响应信息
print("状态码:", response.status_code)
print("响应内容:", response.text)
