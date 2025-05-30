# 문제 상품코드, 상품명, 수량, 단가를 입력받아 금액을 계산한 다음 상품테이블에 저장하는 프로그램이다.
# 처리조건 금액 = 수량 * 단가, 테이블명: sangpum, 컬럼명: 상품코드(code), 상품명(irum), 수량(su), 단가(price), 금액(kumack)
# 상품 정보 입력에 대한 예외처리 기능을 적절히 작성한다. 상품정보 조회, 수정, 삭제시 상품코드를 사용한다. 상품정보를 다루기 위해 상품(Sangpum) 클래스를 정의한다. 상품정보 입력과 수정시 사용하도록 한다.
# 상품 정보 출력할 때 총 판매금액을 누적하여 마지막에 출력한다.

class Sangpum:
    def __init__(self):
        self._code = None
        self._irum = None
        self._su = 0
        self._price = 0
        self._kumack = 0


    def input_sangpum(self):
        self._code = input("상품코드 입력: ")
        self._irum = input("상품명 입력: ")

        while True:
            try:
                self._su = int(input("상품수량 입력: "))
            except Exception as e:
                print("\n 예외발생: ", e.args[0], "\n")
                continue
            else:
                break

        while True:
            try:
                self._price = int(input("상품단가 입력: "))
            except Exception as e:
                print("\n예외발생: ", e.args[0], "\n")
                continue
            else:
                break

    def process_sangpum(self):
        self._kumack = self._su * self._price