while True:
    N=int(input())
    if N==0:
        break
    a = 0
    for i in range(1,N+1):
        a += i*i
    print("{}".format(a))
