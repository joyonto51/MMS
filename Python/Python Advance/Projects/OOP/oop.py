class A():
    a = 1

    def __init__(self):
        print(self.a)



class B(A):
    b = 2

    def __init__(self):
        print(self.b)


class C(B):
    c = 3

    def __init__(self):
        print(self.a, self.b, self.c)

    def get(self):
        self.c = int(input())
        return self.c

    def show(self):
        print(self.get())

    def __del__(self):
        print(self.a, self.b, self.c)


obj = C()
obj.show()
