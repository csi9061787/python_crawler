#爬取動態網頁dcard  (api是get的形式)
import requests
import json
import pprint
from urllib import request
import os
import cloudscraper


dcardFolder = 'dcard/'
if not os.path.exists(dcardFolder):                     #如果這個路徑不存在就新增一個
    os.mkdir(dcardFolder)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}

url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=235214594'
#因為使用get的方式進入dcard被阻擋,故先把post裡的內容以json的形式儲存下來後,在以with的方式打開並讀取(list的形式)
with open('jsondata.json', 'r', encoding='utf-8') as f:
    jsonData = json.loads(f.read())  #list
    #jsonData = json.loads(res.text)  #list

#可以使用cloudscraper越過Dcard的認證
# scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# jsonData = scraper.get(url).json()
# pprint.pprint(jsonData[0])
# print(jsonData[0].keys())

for aticleObj in jsonData:
    title = aticleObj['title']
    aticleUrl = 'https://www.dcard.tw/f/photography/p' + str(aticleObj['id'])        #把id轉為字串
    print(title)
    print(aticleUrl)
    for n, imgInfo in enumerate(aticleObj['mediaMeta']):                   #enumerate使用在迴圈會回傳兩個值:1.值本身  2.值的Index
        tmpImgUrl = imgInfo['url']
        #requests 需要先幫他設定圖片名稱imgPath
        imgPath = dcardFolder + title + '_' +str(n) + '.' + tmpImgUrl.split('.')[-1]
        print('\t',tmpImgUrl)
        #urllib裡的儲存圖片方法,幫每張圖片取名稱,使用標題+ _ + Index值 + . + 副檔名 (圖片網址以.為分隔,取最後一個值), 參數(圖片網址,存放目錄)
        # request.urlretrieve(tmpImgUrl, dcardFolder + title + '_' + str(n) + '.' + tmpImgUrl.split('.')[-1])

        #以requests裡的方式儲存圖片
        resImg = requests.get(tmpImgUrl, headers=headers)
        imgContent = resImg.content
        with open(imgPath, 'wb') as f:
            f.write(imgContent)
    print('============')
