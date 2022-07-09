# -*- coding: UTF-8 -*-
import requests        #导入requests包
url = 'http://www.baidu.com/'
strhtml = requests.get(url)        #Get方式获取网页数据
print(strhtml)#输出响应码
print("strhtml.headers=",strhtml.headers)#输出响应头
#将响应转为UTF-8编码，并显示
strhtml.encoding = 'UTF-8'#print(strhtml.encoding)
print(strhtml.text)