class A(object):
    def __init__(self):
        self.aa = 10
    def print_a(self):
        print(self.aa)

class B(A):
    def __init__(self):
        super().__init__() # A.__init__(self), super(B, self).__init__()
        self.bb = 20
    def print_b(self):
        print(self.bb)

class C(B):
    def __init__(self):
        B.__init__(self) # B.__init__(self), super(C, self).__init__()
        self.cc = 30
    def print_c(self):
        print(self.cc)

if __name__ == '__main__':
    obj = B()
    obj.print_b()