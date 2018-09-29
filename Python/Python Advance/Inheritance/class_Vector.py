class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        print(self.a, self.b)
        print(other.a, other.b)
        return Vector(self.a + other.a, self.b + other.b)

print(v1 + v2)
v1 = Vector(2, 10)
v2 = Vector(5, -2)
v3 = Vector(3, 5)
v4 = Vector(4,6)

