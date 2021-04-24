#爬取PTT電影版文章標題及網址(get)
import requests
from bs4 import BeautifulSoup

#使用for迴圈把網頁標題及網址爬下來
"""userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers = {
'User-Agent':userAgent
}
url = 'https://www.ptt.cc/bbs/movie/index.html'

res = requests.get(url, headers)
soup = BeautifulSoup(res.text, 'html.parser')

titles = soup.select('div.title')
# print(titles)               #每個物件用逗號隔開

for titleSoup in titles:
    title = titleSoup.select('a')[0].text       #因為select取出來的都是list,所以用[0]取出第一個值,再用text的方式只顯示標題
    url = 'https://www.ptt.cc'+ titleSoup.select_one('a')['href']
    print(title)
    print(url)"""

###############################################

#使用for迴圈把網頁標題及網址用頁數的方式顯示出來 (適用於網頁有規律性的情況下)
"""userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers = {
'User-Agent':userAgent
}
url = 'https://www.ptt.cc/bbs/movie/index.html'
page = 9498

for i in range(0,5):
    print('[page:{}]'.format(page))
    res = requests.get(url.format(page), headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    titles = soup.select('div.title')

    for titleSoup in titles:
        title = titleSoup.select('a')[0].text
        urlTitle = 'https://www.ptt.cc'+titleSoup.select_one('a')['href']
        print(title)
        print(urlTitle)

    page -= 1"""

####################################################
#找出上頁的按鈕,並使用迴圈找出前幾頁的標題及網址,效果同上 (適用於網頁不規則的情況下)
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
headers = {
'User-Agent':userAgent
}
url = 'https://www.ptt.cc/bbs/movie/index.html'

for i in range(0,5):            #讓迴圈爬5次上頁
    res = requests.get(url, headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    titles = soup.select('div.title')

    for titleSoup in titles:
        title = titleSoup.select('a')[0].text
        urlTitle = 'https://www.ptt.cc' + titleSoup.select_one('a')['href']
        print(title)
        print(urlTitle)

    lastPageButton = soup.select('a[class="btn wide"]')         #先找出btn wide
    # print(lastPageButton)
    lastPageUrl = 'https://www.ptt.cc' + lastPageButton[1]['href']
    # print(lastPageUrl)
    url = lastPageUrl