while True:
    a,b=map(int,input().split())
    m,n=0,0
    if a==-1 and b==-1:
        break
    if b>a:
        m=100-b+a
        n=b-a
    elif a>b:
        m=100-a+b
        n=a-b
    if n<0:
        n*=-1
    M=m
    if m>n:
        M=n

    print("{}".format(M))
