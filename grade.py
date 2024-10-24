class Grade:
    def __init__(self):
        self.id_n = ""
        self.name = ""
        self.kor = 0
        self.eng = 0
        self.math = 0
        self.total = 0
        self.avg = 0
        self.grade = ""

    def input_grade(self):
        self.id_n = input("Enter your ID: ")
        self.name = input("Enter your name: ")
        self.kor = int(input("Enter your kor: "))
        self.eng = int(input("Enter your eng: "))
        self.math = int(input("Enter your math: "))

    def yield_grade(self):
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3
        if self.avg >= 90:
            self.grade = "A"
        elif self.avg >= 80:
            self.grade = "B"
        elif self.avg >= 70:
            self.grade = "C"
        elif self.avg >= 60:
            self.grade = "D"
        else:
            self.grade = "F"


    def output_grade(self):
        print("%4s  %4s %3d %3d %3d %3d %6.2f   %s"
              % (self.id_n, self.name, self.kor, self.eng, self.math, self.total, self.avg, self.grade))

def f_input(students):
    obj = Grade()
    obj.input_grade()
    obj.yield_grade()
    students.append(obj)
    print("성적정보 입력 완료.")

def f_output(students):
    total = 0
    for student in students:
        student.output_grade()
        total += student.avg
    print("총 학생 수 : %d, 전체 평균 : %.2f\n" % (len(students), total / len(students)))

if __name__ == "__main__":
    students = []
    f_input(students)
    f_output(students)
