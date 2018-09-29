class revrange:
    def __init__(self,n):
        self.n = n
        self.i = n

    def __iter__(self):
        print(10)
        return self

    def __next__(self):    
            if self.n >= 0:
                print("first1")
                self.i = self.n
                self.n = self.n - 1
                return self.i

            else:
                print("first2")
                raise StopIteration

for t in  revrange(7):
    print(t)

