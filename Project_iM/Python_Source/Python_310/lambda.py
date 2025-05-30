# 학번, 이름, 국어, 영어, 수학, 총점, 평균

total_list = []

def print_info():
    #global total_n
    print('\t\t *** 성적표 ***')
    print("======================================")
    print("\t학번\t이름\t국어\t영어\t수학\t총점\t평균\t등급")
    print("======================================")

    total = 0
    for dict in total_list:
        total += dict['avg']
        for k, v in dict.items():
            print(v, end='\t')
        print()

    print("======================================")

    print("\t\t 총 학생 수 : %d, 총 학생 평균 : %d" % (len(total_list), total / len(total_list)))

def get_grade(avg):
    if avg >= 90:
        return '수'
    elif avg >= 80:
        return '우'
    elif avg >= 70:
        return '미'
    elif avg >= 60:
        return '양'
    else:
        return '가'


def input_info():
    info_dict = {}
    info_dict['id'] = input("학번 입력 -> ")
    info_dict['name'] = input("이름 입력 -> ")
    info_dict['kor'] = int(input("국어 점수 입력 -> "))
    info_dict['eng'] = int(input("영어 점수 입력 -> "))
    info_dict['math'] = int(input("수학 점수 입력 -> "))

    info_dict['total'] = info_dict['eng'] + info_dict['math'] + info_dict['kor']
    info_dict['avg'] = round(info_dict['total'] / 3, 2)
    info_dict['grade'] = get_grade(info_dict['avg'])

    total_list.append(info_dict)

def get_info():
    id_n = input("조회할 학번 입력 -> ")
    for dict in total_list:
        if dict['id'] == id_n:
            return dict
    print("입력한 학번에 대한 정보가 없습니다.")

def update_info():
    id_n = input("업데이트할 학번 입력 -> ")
    for dict in total_list:
        if dict['id'] == id_n:
            dict['kor'] = int(input("국어 점수 입력 -> "))
            dict['eng'] = int(input("영어 점수 입력 -> "))
            dict['math'] = int(input("수학 점수 입력 -> "))
            dict['total'] = dict['eng'] + dict['math'] + dict['kor']
            dict['avg'] = round(dict['total'] / 3, 2)
            dict['grade'] = get_grade(dict['avg'])

            print("수정 완료되었습니다.")
            return

    print("입력한 학번에 대한 정보가 없습니다.")

def delete_info():
    id_n = input("삭제할 학번 입력 -> ")
    for dict in total_list:
        if dict['id'] == id_n:
            total_list.remove(dict)
            print("삭제 완료")
            return 1

    print("입력한 학번에 대한 정보가 없습니다.")
    return 0

if __name__ == '__main__':

    while True:
        print("\n\t*** 메뉴 ***")
        print("1. 성적정보 입력\n2. 성적정보 출력\n3. 성적정보 조회\n4. 성적정보 수정\n5. 성적정보 삭제\n6. 프로그램 종료\n")
        print()

        func_n = int(input("메뉴를 선택하세요 : "))
        #total_n = 0

        if func_n == 1:
            input_info()
            #total_n += 1

        elif func_n == 2:
            print_info()

        elif func_n == 3:
            get_dict = get_info()
            print(get_dict)


        elif func_n == 4:
            update_info()

        elif func_n == 5:
            delete_info()
            #if delete_info() == True:
                #total_n -= 1

        elif func_n == 6:
            print("프로그램을 종료합니다.")
            break

        else:
            print("유효하지 않은 입력입니다.")
            continue