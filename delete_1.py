import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()
res = dbcursor.execute('select * from tel order by id desc')

name = input("삭제할 레코드의 이름 입력 : ")
flag = 0
for row in res:
    if row[1] == name:
        dbcursor.execute("delete from tel where name=?", name)
        dbconn.commit()
        flag = 1

if flag == 0:
    print("\n삭제 실패!\n")
else:
    print("\n삭제 성공!\n")

dbcursor.close()
dbconn.close()