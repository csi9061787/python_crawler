from pymongo import MongoClient

#建立連線
client = MongoClient('127.0.0.1', 27017)

#test為要連接的database
db = client.test

#選擇collection
collection = db['test1']
data = {
    1 : 'a'
}

#加入一筆資料
collection.insert_one(data)
print('insert successfully !')
