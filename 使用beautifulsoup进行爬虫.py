#Beautiful Soup 是 python 的一个库，其最主要的功能是从网页中抓取数据。
import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")
#print("response=",response.text)
#print("==========================")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())  #輸出排版後的HTML內容(内容和不使用BeautifulSoup的方法'直接打印response.text一致，只是排版不同)

#以下为搜索时常用的函数方法
# #搜索符合条件的内容
# result = soup.find("h3")
# print("1、soup.find(h3)为============")
# print(result)
# print("符合条件的个数：",len(result))
#
# #搜索所有符合条件的内容
# print("2、soup.find_all(h3)为============")
# result = soup.find_all("h3")
# print(result)
# print("符合条件的个数：",len(result))
#
# #搜索所有符合条件的内容
# print("3、soup.find_all(h3, itemprop=headline)为============")
# result = soup.find_all("h3", itemprop="headline")
# print(result)
# print("符合条件的个数：",len(result))
#
# #搜索所有符合条件的内容 并限制个数
# print("4、soup.find_all(h3, itemprop=headline, limit=3)为============")
# result = soup.find_all("h3", itemprop="headline", limit=3)
# print(result)
# print("符合条件的个数：",len(result))

#返回有h3或p的
print("5、soup.find_all(h3, p)为============")
result = soup.find_all(["h3", "p"])
print(result)
print("符合条件的个数：",len(result))