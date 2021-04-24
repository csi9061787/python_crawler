#爬取政府採購網(POST)
import requests
from bs4 import BeautifulSoup

#用post帶資料,有幾個一定要帶資料的框框就帶幾項
"""url ='http://httpbin.org/post'
headers = {
    'User-Agent':'dnkcnkdjsnsdkv33232xcxzc'
}

data = {
    'Key1':'value1',
    'Key2':'value2'
}

res = requests.post(url, data, headers=headers)
# print(res.text

url = 'http://e2c30d442303.ngrok.io/hello_post'
data = {
    'username':'Angle'
}
res = requests.post(url, data=data)
print(res.text)"""

########################################
#製作post爬取政府採購網
#製作headers
headersStr = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 453
Content-Type: application/x-www-form-urlencoded
Cookie: _ga=GA1.1.1110036226.1611974377; JSESSIONID=0000XXG7IQMTTitV928OiDZVI8w:14iier93p; NSC_xfc_qfstjtufodf=ffffffff09081f7645525d5f4f58455e445a4a423660; cookiesession1=1EF25D71WNA2K4AAPOF28BHAHVUG2E1F; _ga_Y7WTCDJF3D=GS1.1.1612075218.3.1.1612075260.0
Host: web.pcc.gov.tw
Origin: https://web.pcc.gov.tw
Referer: https://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"""

headers = dict()
for row in headersStr.split('\n'):                  #使用for迴圈把[0]:[1]
    headers[row.split(': ')[0]] = row.split(': ')[1]
# print(headers)

dataStr = """
method: search
searchMethod: true
searchTarget: ATM
orgName: 
orgId: 
hid_1: 1
tenderName: 
tenderId: 
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 110/01/29
awardAnnounceEndDate: 110/01/29
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: 
hid_2: 1
gottenVendorName: 
gottenVendorId: 
hid_3: 1
submitVendorName: 
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢"""

data = {row.split(': ')[0]:row.split(': ')[1] for row in dataStr.split('\n') if row !=''}   #1.每一列都是一個row 2.資料來源是dataStr
print(data)

#假設key跟value會變,先取得input的值
userAgent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers = {
    'User-Agent':userAgent
}
url ='https://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
hiddenInput = soup.select('input[type="hidden"]')
print(hiddenInput)

hiddenData = dict()
for i in hiddenInput:                       #取出input(i)裡的name作為key, value作為value
    try:
        hiddenData[i['name']] = i['value']
    except KeyError:
        pass
print(hiddenData)