class Test:
    a, b, c, d = 1, 2, 3, 4

    def __init__(self):
        pass

    def __add__(self, other):
        self.a += other.aprint(A.a)
        return self

A = Test()
B = Test()
C = Test()
print(A.a)
print(B.b)
print(A + B)

print(C.a)


