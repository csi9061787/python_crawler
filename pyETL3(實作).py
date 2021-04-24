from selenium.webdriver import Chrome
import time
#進入PTT八卦版
"""driver = Chrome('./chromedriver')

driver.get('https://www.ptt.cc/bbs/index.html')
#點選進入gossiping的畫面
driver.find_element_by_class_name('board-name').click()
driver.find_element_by_class_name('btn-big').click()"""

########################################
#爬取動態網頁dcard
url = 'https://www.dcard.tw/f'
driver = Chrome('./chromedriver')

driver.get(url)
#找到要輸入內容的框框位置,輸入要打的內容
driver.find_element_by_tag_name('input').send_keys('攝影')
#copy xpath
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/form/button[2]').click()

time.sleep(3)
driver.execute_script('vars = document.documentElement.scrollTop=10000')
time.sleep(3)
driver.execute_script('vars = document.documentElement.scrollTop=1')
time.sleep(3)
driver.execute_script('vars = document.documentElement.scrollTop=10000')

driver.execute_script("return document.getElementsByTagName('html')[0].outerHTML")