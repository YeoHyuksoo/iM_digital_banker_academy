import sqlite3
import time

dbconn = sqlite3.connect('tel.db')

dbcursor = dbconn.cursor()

data = [('홍기자', '010-1111-1111', '서울', str(time.asctime(time.localtime(time.time()))), '테스트1'),
        ('한기자', '010-2222-2222', '수원', str(time.asctime(time.localtime(time.time()))), '테스트2'),
        ('길기자', '010-3333-3333', '경주', str(time.asctime(time.localtime(time.time()))), '테스트3'),]

sql = "insert into tel (name, tel, addr, input_time, memo) values (?, ?, ?, ?, ?)"

# sql = "insert into tel values (null, ?, ?, ?, ?, ?)"
dbcursor.executemany(sql, data)

dbconn.commit()

for row in dbcursor.execute('select * from tel'):
    print(row)

dbcursor.close()
dbconn.close()