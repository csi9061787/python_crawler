'''
題目:進入這個網址 submit後 不能出現Bad request.
(要出現 以下就是成功
    "Status": "OK",
    "Success": true,
    "td": 1.0664231777191162

'''

import requests
from bs4 import BeautifulSoup

url ='http://bcc4eb6b1de2.ngrok.io/practice/ceb102'

headers ={
    'user-agent':'123'
}

ss = requests.session()

res = ss.get(url,headers=headers)
# print(res.text)
soup=BeautifulSoup(res.text,'html.parser')
print(soup)

#抓出hidden value
# print(soup.select('input'))
key =soup.select('input')[1]['name']
value =soup.select('input')[1]['value']
# print(key,value)

# 有兩個要帶的東西，一個是hidden value，另一個是你要在框框輸入的東西
data ={key:value,'pwd':'name123'}
res =ss.post(url,data=data,headers=headers)
# print(res.text)