class Sungjuk:
    def __init__(self):
        self.hakbun = ""
        self.irum = ""
        self.kor = 0
        self.eng = 0
        self.math = 0
        self.tot = 0
        self.avg = 0.0
        self.grade = ""

    def input_sungjuk(self):
        self.hakbun = input("학번 입력 : ")
        self.irum = input("이름 입력 : ")
        self.kor = int(input("국어점수 입력 : "))
        self.eng = int(input("영어점수 입력 : "))
        self.math = int(input("수학점수 입력 : "))

    def process_sungjuk(self):
        self.tot = self.kor + self.eng + self.math
        self.avg = self.tot / 3
        if self.avg >= 90:
            self.grade = "수"
        elif self.avg >= 80:
            self.grade = "우"
        elif self.avg >= 70:
            self.grade = "미"
        elif self.avg >= 60:
            self.grade = "양"
        else:
            self.grade = "가"

    def output_sungjuk(self):
        print("%4s  %4s   %3d    %3d    %3d     %3d   %6.2f     %s"
              % (self.hakbun, self.irum, self.kor, self.eng, self.math,
                 self.tot, self.avg, self.grade))

if __name__ == "__main__":
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()
    print("\n                     *** 성적표 ***")
    print("=========================================================")
    print("학번    이름    국어    영어    수학    총점    평균     등급")
    print("=========================================================")
    obj.output_sungjuk()
    print("=========================================================")