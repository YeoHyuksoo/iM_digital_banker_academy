from sangpum import Sangpum
import pymysql

def create_db_table():
    global dbconn, dbcursor
    dbconn = pymysql.connect(host='localhost',  # 도메인
                           port=3306,
                           user='root',  # MYSQL 내 모든 데이터베이스에 권한 가지고있음
                           password='123456',
                           db='prod_db',
                           charset='utf8')
    dbcursor = dbconn.cursor()

    dbcursor.execute('create table if not exists product \
        (code char(10) primary key, \
        name char(10), \
        amount integer, \
        price integer, \
        total integer);')

def f_menu():
    print("\t*** 메뉴 ***")
    print("1. 상품정보 입력")
    print("2. 상품정보 출력")
    print("3. 상품정보 조회")
    print("4. 상품정보 수정")
    print("5. 상품정보 삭제")
    print("6. 프로그램 종료")

def input_product():
    obj = Sangpum()
    print()
    obj.input_sangpum()
    obj.process_sangpum()

    global dbconn, dbcursor

    sql = 'insert into product (code, name, amount, price, total) \
            values(%s, %s, %s, %s, %s);'
    try:
        dbcursor.execute(sql, (obj._code, obj._irum, obj._su, obj._price, obj._kumack))
        dbconn.commit()
        print("\n상품정보 입력 성공\n")

    except Exception as e:
        print("예외발생: ", e.args[0], "\n")


def output_product():
    total_price = 0

    dbcursor.execute("select count(*) from product;")
    row = dbcursor.fetchone()[0]
    if row == 0:
        print("\n출력할 상품 데이터 없음!!\n")
        return

    dbcursor.execute("select * from product;")
    res = dbcursor.fetchall()

    print("\n             *** 상품 리스트 ***")
    print("============================================")
    print("상품코드      상품명       수량       단가       금액")
    print("============================================")

    for obj in res:
        total_price += obj[4]
        print("%s      %10s      %d       %d     %d"
              %(obj[0], obj[1], obj[2], obj[3], obj[4]))
    print("============================================")
    print("           총 판매금액 = %d\n" % total_price)


def search_product():
    code = input("조회할 상품코드를 입력하세요( ex) 0001, 1234 ) => ")

    dbcursor.execute("select * from product where code = %s;", code)
    row = dbcursor.fetchone()
    if row:
        print("\t\t *** 조회 결과 ***")
        print("\n==================================================")
        print("상품코드     상품명       수량       단가       금액")
        print("==================================================")
        print("%s       %10s      %d     %d     %d"
              % (row[0], row[1], row[2], row[3], row[4]))
        print("==================================================\n")

    else:
        print("조회할 상품코드 %s가 없습니다." % code)


def update_product():
    code = input("수정할 상품코드를 입력하세요( ex) 0001, 1234 ) => ")
    dbcursor.execute("select * from product where code = %s;", code)
    row = dbcursor.fetchone()

    if row:
        obj = Sangpum()
        obj._code = row[0]
        obj._irum = input("\n상품명을 입력하세요: ")
        obj._su = int(input("상품수량을 입력하세요: "))
        obj._price = int(input("상품단가를 입력하세요: "))
        obj.process_sangpum()

        sql = "update product set name = %s, amount = %s, price = %s, total = %s \
                    where code = %s;"
        dbcursor.execute(sql, (obj._irum, obj._su, obj._price, obj._kumack, obj._code))
        dbconn.commit()

        print("\n상품정보 수정 성공!!\n")

    else:
        print("\n수정할 상품정보 %s가(이) 없습니다.\n" % code)


def delete_product():
    code = input("삭제할 상품코드를 입력하세요: ")
    dbcursor.execute("select * from product where code = %s;", code)
    row = dbcursor.fetchone()

    if row:
        sql = "delete from product where code = %s;"
        dbcursor.execute(sql, code)
        dbconn.commit()
        print("\n상품삭제 성공!!\n")

    else:
        print("\n삭제할 상품코드 %s가(이) 없습니다.\n" % code)



if __name__ == "__main__":
    create_db_table()
    global dbconn, dbcursor
    while True:
        f_menu()
        menu = int(input("\n메뉴를 입력하세요: "))
        if menu == 1:
            input_product()
        elif menu == 2:
            output_product()
        elif menu == 3:
            search_product()
        elif menu == 4:
            update_product()
        elif menu == 5:
            delete_product()
        elif menu == 6:
            print("\n프로그램을 종료합니다.\n")
            dbcursor.close()
            dbconn.close()
            break
        else:
            print("\n메뉴를 다시 입력하세요!!\n")

