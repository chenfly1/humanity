import requests

# 请求的 URL
url = "https://testnet.humanity.org/api/claim/referralRewards"

# 请求头
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "authorization": "",
    "content-length": "0",
    "cookie": "QueueITAccepted-SDFrts345E-V3_humanityprotocol=EventId%3Dhumanityprotocol%26QueueId%3D44b20842-13d0-4be8-a1b8-bd14b4baf4f4%26RedirectType%3Dqueue%26IssueTime%3D1731857430%26Hash%3Dbbec3c989fca03aab9bece8b6b144742ad6498e95ccba2fb17c94b81b2f4b511",
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
