from sungjuk import Sungjuk
import sqlite3
def create_table():
    dbconn = sqlite3.connect('sungjuk.db')
    dbcursor = dbconn.cursor()
    dbcursor.execute("""CREATE TABLE IF NOT EXISTS sungjuk (
        hakbun text primary key,
        irum text,
        kor integer,
        eng integer,
        math integer,
        tot integer,
        avg real,
        grade text
        )""")

    dbcursor.close()
    dbconn.close()

def f_menu():
    print(" *** 메뉴 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")

def f_input():
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()

    dbconn = sqlite3.connect('sungjuk.db')
    dbcursor = dbconn.cursor()
    data = (obj.hakbun, obj.irum, obj.kor, obj.eng, obj.math, obj.tot, obj.avg, obj.grade)

    sql = "insert into sungjuk (hakbun, irum, kor, eng, math, tot, avg, grade) values (?, ?, ?, ?, ?, ?, ?, ?)"
    dbcursor.execute(sql, data)
    dbconn.commit()

    dbcursor.close()
    dbconn.close()

def f_output():
    total_avg = 0

    dbconn = sqlite3.connect('sungjuk.db')
    dbcursor = dbconn.cursor()

    dbcursor.execute("SELECT count(*) FROM sungjuk")
    cnt = dbcursor.fetchone()[0]
    if cnt == 0:
        print("\n데이터 없음!")
        return

    else:
        dbcursor.execute("SELECT * FROM sungjuk order by hakbun asc")
        res = dbcursor.fetchall()

        print("\n                      *** 성적표 ***")
        print("============================================================")
        print("학번    이름    국어    영어    수학    총점    평균     등급")
        print("============================================================")
        for obj in res:
            total_avg += obj[6]
            print("%4s  %4s   %3d    %3d    %3d     %3d   %6.2f     %s"
                  % (obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6], obj[7]))
        print("============================================================")
        print("            총학생수 = %d,  전체 평균 = %.2f\n" % (cnt,
                                                          total_avg / cnt))


def f_search():
    dbconn = sqlite3.connect('sungjuk.db')
    dbcursor = dbconn.cursor()

    hakbun = input("\n조회할 학번 입력 : ")

    sql = "SELECT * FROM sungjuk where hakbun = ?"
    dbcursor.execute(sql, (hakbun,))

    res = dbcursor.fetchall()
    if len(res) == 0:
        print("입력한 학번 데이터가 없습니다.")
    else:
        print("\n학번    이름    국어    영어    수학    총점    평균     등급")
        print("=========================================================")
        for obj in res:
            print(obj)
        print("=========================================================\n")

def process_sungjuk(kor, eng, math):
    tot = kor + eng + math
    avg = tot / 3
    if avg >= 90:
        grade = "수"
    elif avg >= 80:
        grade = "우"
    elif avg >= 70:
        grade = "미"
    elif avg >= 60:
        grade = "양"
    else:
        grade = "가"
    return tot, avg, grade

def f_update():
    dbconn = sqlite3.connect('sungjuk.db')
    dbcursor = dbconn.cursor()

    hakbun = input("\n수정할 학번 입력 : ")

    sql = "SELECT * FROM sungjuk where hakbun = ?"
    dbcursor.execute(sql, (hakbun,))

    res = dbcursor.fetchone()
    if res is None:
        print("수정할 학번 데이터가 없습니다.")
    else:
        kor = int(input("국어점수 입력: "))
        eng = int(input("영어점수 입력: "))
        math = int(input("수학점수 입력: "))
        tot, avg, grade = process_sungjuk(kor, eng, math)
        dbcursor.execute("update sungjuk set kor=?, eng=?, math=?, tot=?, avg=?, grade=? where hakbun=?",
                         (kor, eng, math, tot, avg, grade, hakbun))

        dbconn.commit()
        print("\n학번 %s 성적정보 수정 성공!!\n" % hakbun)

    dbcursor.close()
    dbconn.close()

def f_delete():
    pass

if __name__ == "__main__":
    # students = []
    create_table()
    while True:
        f_menu()
        menu = int(input("\n메뉴를 선택하세요 : "))

        if menu == 1:
            f_input()
        elif menu == 2:
            f_output()
        elif menu == 3:
            f_search()
        elif menu == 4:
            f_update()
        elif menu == 5:
            f_delete()
        elif menu == 6:
            print("\n프로그램 종료...")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!!\n")