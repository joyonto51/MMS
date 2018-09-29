
class Person():
    def __init__(self):
        print('In Abstract Class')


class Student(Person):
    def __init__(self):
        print('In Student Class')


class Teacher(Person):
    def __init__(self):
        print('In Teacher Class')


P = Person()
S = Student()
T = Teacher()
