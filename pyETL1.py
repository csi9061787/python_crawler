from urllib import request  #使用urllib裡的request
from bs4 import BeautifulSoup
import requests

"""userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
                                                #從F12的useragent複製過來宣告變數
headers = {
    'User-Agent':userAgent
}                                                #把剛才新增的變數變成字典(Json)
url = 'https://www.ptt.cc/bbs/joke/index.html'
req = request.Request(url=url, headers=headers)  #再宣告一個變數放url跟headers,製作成一個Request的物件
res = request.urlopen(req)
html = res.read().decode('utf-8')           #把res用read並轉換成html的字串 (回傳網頁的html(此時為bytes),使用decode轉換為字串)
print(html) """

#########################################################

"""userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers = {
'User-Agent':userAgent
}
url = 'https://www.ptt.cc/bbs/joke/index.html'

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')       #指定用html.parser轉碼
#print(soup)

logo = soup.findAll('a', {'id':'logo'})         #使用字典格式的查詢
logo = soup.findAll('a', id='logo')             #直接使用id=''的方式查詢
print(logo[0].text)   #text代表標籤裡面的內容
print('https://www.ptt.cc' + logo[0]['href'])   #把logo當成字典,取出裡面的href的value, 前面加上'網址'+ = 完整的網址

bbsContent = soup.findAll('div', class_='bbs-content')  #使用第二種方式查詢遇到class這種python保留字元,需加個_改名
print(bbsContent[0].findAll('div'))                     #若是要找div裡面的標籤,它是不會去定位最外層的標籤,會從下面一層開始找
print(bbsContent[0].findAll('a'))                       #回傳會以list的形式

#########################
print('================')

bbsContent = soup.select('div[class="bbs-content"]')    #使用select查詢,第一種方式
bbsContent = soup.select('div.bbs-content')             #第二種方式查詢,與上面結果相同
print(bbsContent[0].findAll('a'))   """                 #find跟select可以混著用

####################################################3

"""userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers = {
'User-Agent':userAgent
}
url = 'https://www.ptt.cc/bbs/joke/index.html'
res = requests.get(url, headers)                        #requests可以直接使用變數帶入
soup = BeautifulSoup(res.text, 'html.parser')           #用requests可以直接用res.text的狀態
print(soup)"""

