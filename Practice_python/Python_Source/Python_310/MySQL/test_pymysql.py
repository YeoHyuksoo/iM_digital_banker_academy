import pymysql

conn = pymysql.connect(host = 'localhost', # 도메인
                       port = 3306,
                       user = 'root', # MYSQL 내 모든 데이터베이스에 권한 가지고있음
                       password = '123456',
                       db = 'prod_db',
                       charset = 'utf8')

cursor = conn.cursor()

# sql = 'select * from usertbl'
# cursor.execute(sql)
#
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

sql = 'insert into usertbl values (%s, %s, %s, %s, %s, %s, %s, %s);' # %s로 무조건 인자를 받는다.

try:
    userID = input("아이디 입력 => ")
    name = input("이름 입력 => ")
    birthYear = int(input("생년 입력 => "))
    addr = input("주소 입력 => ")
    mobile1 = input("휴대폰번호(앞자리) 입력 => ")
    mobile2 = input("휴대폰번호(뒷자리) 입력 => ")
    height = int(input("키 입력 => "))
    mDate = input("가입날짜( ex) 2024-11-01) 입력 => ")

    cursor.execute(sql, (userID, name, birthYear, addr, mobile1, mobile2, height, mDate))

    conn.commit()

    sql = 'select * from usertbl'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print("\n입력 오류!!!", e.args[0], "\n")

finally:
    cursor.close()
    conn.close()




# cursor.close()
# conn.close()


