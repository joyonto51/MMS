n = int(input())
def f(n):
        m = len(str(n))
        x = []
        b = 0
        if m>1:
            for i in range(m):
                 n=str(n)
                 x += map(int, n[i])
                 b = sum(x)
            if len(str(b))>1:
                b = int(b)
                f(b)
            else:
                print("{}".format(b))
        else:
            print("{}".format(n))
while True:
    if n!=0:
        f(n)
        n = int(input())
    else:
        break



