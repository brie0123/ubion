import pymysql
conn = pymysql.connect(host = 'localhost',user = 'root',password = 'apple123!!',db = 'shoppingDB',charset='utf8')
cur = conn.cursor()

cur.execute("SELECT * FROM userTable")

print("사용자ID 사용자이름 이메일 출생연도")
print("--------------------------------------")

while (True):
    row = cur.fetchone()
    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%s %s %s %d" %(data1, data2, data3, data4))
    
conn.close()

