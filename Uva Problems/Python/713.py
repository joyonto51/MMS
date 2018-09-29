T = int(input())
for i in range(T):
    a,b=map(str,input().split())
    x = int(a[::-1])
    y = int(b[::-1])
    w = str(x+y)
    z = int(w[::-1])
    print("{}".format(z))
