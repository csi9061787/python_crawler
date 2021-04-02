import pymysql
from sqlalchemy import create_engine
import pandas as pd


# #第一種:連線到MySQL 創建Table
# 建立連線
# db = pymysql.connect(
#   host = "127.0.0.1",
#   user = "root",
#   password = "7871609",
#   database = "food",
#   cursorclass=pymysql.cursors.DictCursor
#   )
# cur = db.cursor()
#
#
#
# # Create table  # VARCHAR()  #INT() #DECIMAL()
# cur.execute("""CREATE TABLE Nutrition
#             (ID INT(20) PRIMARY Key,
#              Classification VARCHAR(10),
#              Name  VARCHAR(15) NOT NULL,
#              Content VARCHAR(30),
#              Calories DECIMAL(7,2),
#              Moisture_g DECIMAL(7,2),
#              Saturated_fat_g DECIMAL(7,2),
#              Carbohydrates_g DECIMAL(7,2),
#              Total_sugar_g DECIMAL(7,2),
#              lactose_g DECIMAL(7,2),
#              calcium_mg DECIMAL(7,2))"""
#             )
# #提交動作
# cur.commit()
# #結束連線
# cur.close()
#---------------------------------------------------------------------------------------------------------------------------

#第二種:使用to_sql把dataframe放進table
# 建立連線
engine = create_engine("mysql+pymysql://{}:{}@{}/{}?charset={}".format('root', '7871609', '127.0.0.1:3306', 'food','utf8'))
con = engine.connect()

#讀取要放的資料
df = pd.read_excel('C:/Users/CEB10202/Desktop/食品成分表.xlsx')

#選擇需要的columns,rows
df2 = df[['樣品編號','食品分類','樣品名稱','內容物描述','熱量(kcal)','水分(g)','飽和脂肪(g)','總碳水化合物(g)','糖質總量(g)','乳糖(g)','鈣(mg)']][0:2092]

pd.io.sql.to_sql(df2,'nutrition', con=con, if_exists='replace', index= False)
print("Write to MySQL successfully!")
