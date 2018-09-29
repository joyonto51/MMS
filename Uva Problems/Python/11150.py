while True:
    try:
        n=int(input())
    except:
        break
    N=n
    while True:
        x = n%3
        n = (n//3)
        N+=n
        n+=x
        if n==2:
            N+=1
        if n<3:
            break
    print("{}".format(N))
