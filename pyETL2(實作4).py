#帶cookies或session進入網域
import requests
from bs4 import BeautifulSoup

#帶cookies進入網頁 #第一種寫法 每一次requests都要加上一個cookies,每一個requests都是一個獨立的連線
"""url ='https://www.ptt.cc/bbs/Gossiping/index.html'
cookies = {
    'over18':'1'
}
res = requests.get(url, cookies=cookies)

print(res.text)"""

##########################################
#使用session,紀錄使用者的使用狀態,比較像人類
"""url ='https://www.ptt.cc/bbs/Gossiping/index.html'
ss = requests.session()
ss.cookies['over18'] = '1'
res = ss.get(url)
print(res.text)"""

#########################################
#取得ptt八卦版的cookies,並抓取cookies何時被綁定,並利用這樣的方式進入網站 (適用於cookies很常變化,沒有規律性)
loadingPageUrl ='https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
over18Url = 'https://www.ptt.cc'
pttUrl = 'https://www.ptt.cc/bbs/Gossiping/index.html'

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers = {
'User-Agent':userAgent
}

ss = requests.session()

resloadingPage = ss.get(loadingPageUrl, headers=headers)
souploadingPage = BeautifulSoup(resloadingPage.text, 'html.parser')

data = dict()
#for hidden value
hiddenKey = souploadingPage.select('input')[0]['name']
hiddenValue = souploadingPage.select('input')[0]['value']
data[hiddenKey] = hiddenValue

#for button
buttonKey = souploadingPage.select('button')[0]['name']
buttonValue = souploadingPage.select('button')[0]['value']
data[buttonKey] = buttonValue
print(data)
print(ss.cookies)                       #看身上目前有哪些cookies

#Get cookies
over18Url += souploadingPage.select('form')[0]['action']        #針對cookies的網域改變
ss.post(over18Url, data=data)
print(ss.cookies)                       #多了一個cookies

res = ss.get(pttUrl, headers=headers)
print(res.text)                         #成功進入ptt八卦版
