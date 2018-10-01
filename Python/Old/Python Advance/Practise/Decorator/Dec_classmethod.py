class My_class:

    def __init__(self):
        pass
    def square(self,x):
        return x**2

    @classmethod
    def cube(self,x):
        return x**3
    if __name__== "__main__":
        my_class = My_class
        pritn(mylass.square())
        print(my_class.cube(3))
        print()