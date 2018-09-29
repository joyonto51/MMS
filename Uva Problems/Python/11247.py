import math
while True:
    m,x = map(int,input().split())
    N=0
    if m==0 and x==0:
        break
    if (1>=x or x>=100) or m<=1:
        print("Not found")
    elif m<x:
        y=100-x
        n =((m*100)/y)-1
        v = n//m
        N = n-v
        if N%1>=0.5:
            N=int(N)+1
        if N<=m:
            print("Not found")
        else:
            N=int(N)
        print("{}".format(N))

    else:
        y=100-x
        n =(m*100)/y
        n = math.ceil(n)
        N = n-2
        print("{}".format(N))
