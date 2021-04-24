#爬取動態網頁(科技報橘) api是POST形式
import requests
import json
from bs4 import BeautifulSoup
import time


url='https://buzzorange.com/techorange/wp-admin/admin-ajax.php'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}

data ={
    'action': 'fm_ajax_load_more',
    'nonce': '64b097bf9a',
    'page': 1
}
for p in range(0,3):
    print('[Page:{}]'.format(data['page']))
    isRequestSuccess = False
    while isRequestSuccess == False:
        try:
            res = requests.post(url, headers=headers, data=data)
            # jsonData = json.loads(res.text)
            jsonData = res.json()
        except json.decoder.JSONDecodeError:
            time.sleep(3)
        else:
            isRequestSuccess = True

    htmlStr = jsonData['data']
    soup = BeautifulSoup(htmlStr, 'html.parser')

    for titleSoup in soup.select('h4[class="entry-title"]'):
        # print(titleSoup.a)
        title = titleSoup.a.text
        articleUrl = titleSoup.a['href']
        print(title)
        print(articleUrl)
        print('===============')
    data['page'] += 1
    time.sleep(3)