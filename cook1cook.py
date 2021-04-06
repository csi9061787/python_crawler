import bson
import requests
from bs4 import BeautifulSoup
import os
import time
import json
from pymongo import MongoClient
from bson import BSON
import re

#建立連線
client = MongoClient('127.0.0.1', 27017)
#要連線的DB
db = client.food
collection = db['cook1cook']


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
url = 'https://cook1cook.com/category'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

for categories in soup.select('div[class=category_list]'):          #抓取分類列表
    c_Title = categories.select('a[href]')[0].text       #抓取主分類標題
    # url_ctitle = categories.select_one('a')['href']       #抓取主分類標題url
    s_Title = categories.select('p[class="sub_category_title"]')[0]('a')[0].text         #抓取子分類標題
    url_stitle = categories.select_one('div > p > a')['href']             #抓取子分類標題url
    # c_id = url_ctitle.split('/')[-1]             #用url最後的數字當作主分類標題id
    s_id = url_stitle.split('/')[-1]            #用url最後的數字當作子分類標題id
#===============================================================================
    SubCategories = {s_id:s_Title}
    # page = 1
    page = 1138
#===============================================================================
    # 建立儲存圖片的資料夾
    Img_Dir_Path = './cook1cook_img/SubCategory_' + s_id
    if not os.path.exists(Img_Dir_Path):
        os.makedirs(Img_Dir_Path)

    #建立儲存jsonfile的資料夾
    JsonFile_Dir_Path = './cook1cook_jsonfile'
    if not os.path.exists(JsonFile_Dir_Path):
        os.makedirs(JsonFile_Dir_Path)
    while True:
        try:
            SubCategoryUrl = 'https://cook1cook.com/category/{}/{}'.format(s_id,page)           #子分類
            SubCategoryRes = requests.get(url=SubCategoryUrl, headers=headers)
            SubCategorySoup = BeautifulSoup(SubCategoryRes.text, 'html.parser')
            Total_Recipes = SubCategorySoup.select('div[class="recipe-info col-md-8"]')

            for recipe in Total_Recipes:
                title = recipe.select('h2 > a[title]')[0].text.replace(' ', '').replace('\n', '')  # 標題名稱
                content_url = recipe.select_one('a')['href']# 內容網址
                RecipeID = content_url.split('/')[-1] # 食譜ID
#--------------------------開始抓食譜---------------------------------------------------------------
                content_res = requests.get(content_url, headers=headers)  # 食譜內容爬蟲
                content_soup = BeautifulSoup(content_res.text, 'html.parser')
                content_like = content_soup.select('span[id="like_times"]')[0].text    #按讚數
                content_eye = content_soup.select('li')[16].text.strip()               #瀏覽數
                img_url_t = content_soup.select('div[class="recipe-picture-frame"]')[0]
                img_url = img_url_t.select_one('a')['href']                         #抓取圖片網址
                Img_conetent = requests.get(img_url, headers).content
                if not os.path.exists(Img_Dir_Path + '/' + RecipeID + '.jpg'):      #儲存到資料夾裡
                    with open(Img_Dir_Path + '/' + RecipeID + '.jpg', 'wb') as f:
                        f.write(Img_conetent)

                Author = content_soup.select('a[class="hide"]')[0].text             #作者名字
                AuthorID = content_soup.select_one('div[class="info"] > span > a')['href'].split('/')[-1]

                Introduction = content_soup.select('div[class="recipe-description"]')[0].text       #抓取食譜介紹

                IngredientName = [x.text.strip().replace('.','-') for x in content_soup.select('ul[class="group_1"]')[0].select('span[class="pull-left ingredient-name"]')]#名稱
                IngredientUnit = [y.text.strip().replace('.','-') for y in content_soup.select('ul[class="group_1"]')[0].select('span[class="pull-right ingredient-unit"]')] # 數量
                IngredientDict = dict(zip(IngredientName, IngredientUnit))            #抓取食材名稱及份量並加入到dict裡

                CookingSteps = [x.text.strip() for x in content_soup.select('div[class="media"] > div[class="media-body"]')]       #抓取食譜步驟

                Servings = content_soup.select('h2 > span[class="pull-left"] > span')[0].text          #抓取分量

                CookingTime = content_soup.select('h2 > span[class="pull-right"] > span')[0].text.strip()               #抓取烹飪時間

                RecipeInformation = {
                    'Recipeid': RecipeID,  # 食譜ID
                    'CategoryName': c_Title,  # 主類別名稱
                    'SubCategoryID': s_id,  # 子類別ID
                    'SubCategoryName': s_Title,  # 子類別名稱
                    'RecipeName': title,  # 食譜標題名稱
                    'RecipeURL': 'https://cook1cook.com/category/{}'.format(RecipeID),   #食譜網址
                    'Introduction': Introduction, # 食譜介紹
                    'AuthorID': AuthorID,  # 作者ID
                    'Author': Author,  # 作者
                    'Servings': Servings,  # 份量
                    'CookingTime': CookingTime,  # 烹飪時間
                    'Ingredient': IngredientDict,  # 所需食材及各食材份量
                    'CookingSteps': CookingSteps,  # 烹飪方法
                    'LikeStat': content_like,  # 按讚數
                    'ContentEyes': content_eye  # 瀏覽量
                }
                print(RecipeInformation)
                collection.insert_one(RecipeInformation)

        except IndexError:
            print(IndexError)
            pass
            if page % 5 == 0:
                try:
                    with open('./cook1cook_jsonfile/page_{}.txt'.format(page),'a') as jsonfile:              #每爬取5頁就寫入一個jsonfile
                        json.dump(RecipeInformation, jsonfile,indent=2)
                except TypeError:  # 有時候爬到最後幾頁會出現可能都是廣告html與正常食譜網頁不同，會出現都是空字串的list，在匯入Mongodb會出現TypeError，
                    pass  # 若出現該情況則用TryException將例外排除
                except bson.errors.InvalidDocument:
                    pass
            print('ok')
            print('----------------------------------------------------')
        time.sleep(10)
        page += 1
        print('===========================================================================')
        print('now page: {}'.format(page))
        if page == 3000:
            break
    print('-----Finish-----')
