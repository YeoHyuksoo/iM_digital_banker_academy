import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()
res = dbcursor.execute('select * from tel order by id desc')

name = input("수정할 레코드의 이름 입력 : ")
flag = 0
for row in res:
    if row[1] == name:
        tel = input("전화번호 : ")
        addr = input("주소 : ")
        memo = input("메모 : ")
        dbcursor.execute("update tel set tel=?, addr=?, memo=? where name=?", (tel,addr,memo, name,))
        dbconn.commit()
        flag = 1

if flag == 0:
    print("\n수정 실패!\n")
else:
    print("\n수정 성공!\n")

dbconn.close()