import requests

url = "http://httpbin.org/post"
data = {
    "name": "liyuanjing",
    "age": "29"
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
result = requests.post(url=url, timeout=1, headers=headers, data=data)
# 打印网页源代码
print(result.text)
# 将其转换为json
print(result.json())