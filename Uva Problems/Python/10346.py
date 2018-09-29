while True:
    try:
        n,k=map(int,input().split())
    except:
        break
    N=n
    while True:
        x = n%k
        n = (n//k)
        N+=n
        n += x
        if n<k:
            break
    print("{}".format(N))
