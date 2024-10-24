class Product:
    def __init__(self):
        self.id_code = None
        self.name = None
        self.amount = 0
        self.unit_price = 0
        self.total_price = 0

    def get_code(self):
        return self.id_code

    def set_code(self, code):
        self.id_code = code

    code = property(get_code, set_code)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    name = property(get_name, set_name)

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    amount = property(get_amount, set_amount)

    def get_unit(self):
        return self.unit_price

    def set_unit(self, unit):
        self.unit_price = unit

    unit = property(get_unit, set_unit)

    def get_total(self):
        return self.total_price

    def set_total(self, total):
        self.total_price = total

    total = property(get_total, set_total)

    def input_number(self):
        while True:
            try:
                self.amount = int(input("수량 입력 : "))
            except Exception as e:
                print("\n 숫자 입력 해주세요.", e.args[0], "\n")
            else:
                break

        while True:
            try:
                self.unit_price = int(input("단가 입력 : "))
            except Exception as e:
                print("\n숫자 입력해주세요.", e.args[0], '\n')
            else:
                break

    def input_data(self):
        self.id_code = input("상품코드 입력 : ")
        self.name = input("상품명 입력 : ")
        self.input_number()

    def cal_total(self):
        self.total_price = self.amount * self.unit_price



"""
    def input_product(self):
        self.id_code = input("상품코드 입력 : ")
        self.name = input("상품명 입력 : ")
        self.amount = int(input("수량 입력 : "))
        self.unit_price = int(input("단가 입력 : "))
        self.total_price = self.amount * self.unit_price


    def output_product(self):
        print("%4s  %4s   %3d    %3d    %3d"
              % (self.id_code, self.name, self.amount, self.unit_price, self.total_price))
"""
