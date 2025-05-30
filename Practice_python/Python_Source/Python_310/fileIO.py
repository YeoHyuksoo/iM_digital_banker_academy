"""
fp = open("text.txt", "wt", encoding="utf-8")
fp.write("%d\n" % 1)
fp.write("%.2f\n" % 3.14)
fp.write("Hello world!\n")
fp.write("안녕 파이썬!")
fp.close()
"""

fp = open("text.txt", "rt", encoding="utf-8")
contents = fp.read()
print(contents)
fp.close()

def divide(m, n):
    try:
        result = m / n
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except:
        print("zero division error 이외의 예외가 발생했습니다.")

    else:
        print("결과 나왔습니다.")
        return result
    finally:
        print("나눗셈 연산입니다.")

if __name__ == '__main__':
    result = divide(5, 2)
    print(result)
    print()
    result = divide(3, 0)
    print(result)
    print()
    result = divide(None, 2)
    print(result)