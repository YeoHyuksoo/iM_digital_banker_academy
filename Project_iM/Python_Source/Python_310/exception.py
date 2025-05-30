def divide(m, n):
    try:
        result = m / n
    except ZeroDivisionError as e:
        print("zero division error", e.args[0])


def some_func():
    print("1~10사이 수를 입력하세요: ")
    num = int(input())
    if num < 1 or num > 10:
        raise Exception("유효하지 않은 숫자입니다.: {0}".format(num))
    else:
        print("{0} 입력받았습니다.".format(num))

def some_func_caller():
    try:
        some_func()
    except Exception as err:
        print("")