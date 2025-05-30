from sungjuk import Sungjuk

def f_menu():
    print(" *** 메뉴 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")


def f_input(f_students):
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()
    f_students.append(obj)
    print("\n성적정보 입력 성공!!\n");

def f_output(f_students):
    total_avg = 0
    if len(f_students) == 0:
        print("\n출력할 데이터가 없습니다!!!\n")
        return

    print("\n                      *** 성적표 ***")
    print("============================================================")
    print("학번    이름    국어    영어    수학    총점    평균     등급")
    print("============================================================")
    for obj in f_students:
        total_avg += obj.avg
        obj.output_sungjuk()
    print("============================================================")
    print("            총학생수 = %d,  전체 평균 = %.2f\n" % (len(f_students),
                                                total_avg / len(f_students)))

def f_search(f_students):
    hakbun = input("\n조회할 학번 입력 : ")
    for data in f_students:
        if data.hakbun == hakbun:
            print("\n학번    이름    국어    영어    수학    총점    평균     등급")
            print("=========================================================")
            data.output_sungjuk()
            print("=========================================================\n")
            break
    else:
        print("\n조회할 학번 %s가 없습니다!!\n" % hakbun)


def f_update(f_students):
    hakbun = input("\n수정할 학번 입력 : ")
    for data in f_students:
        if data.hakbun == hakbun:
            data.kor = int(input("국어점수 입력 : "))
            data.eng = int(input("영어점수 입력 : "))
            data.math = int(input("수학점수 입력 : "))
            data.process_sungjuk()
            print("\n학번 %s 성적정보 수정 성공!!\n" % data.hakbun)
            break
    else:
        print("\n수정할 학번 %s가 없습니다!!\n" % hakbun)




def f_delete(f_students):
    hakbun = input("\n삭제할 학번 입력 : ")
    for data in f_students:
        if data.hakbun == hakbun:
            f_students.remove(data)
            print("\n학번 %s 성적정보 삭제 성공!!\n" % data.hakbun)
            break
    else:
        print("\n삭제할 학번 %s가 없습니다!!\n" % hakbun)


if __name__ == "__main__":
    students = []
    while True:
        f_menu()

        menu = int(input("\n메뉴를 선택하세요 : "))
        if menu == 1:
            f_input(students)
        elif menu == 2:
            f_output(students)
        elif menu == 3:
            f_search(students)
        elif menu == 4:
            f_update(students)
        elif menu == 5:
            f_delete(students)
        elif menu == 6:
            print("\n프로그램 종료...")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!!\n")