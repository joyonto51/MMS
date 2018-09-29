while True:
    n=int(input())
    if n==0:
        break
    while True:
        i=0
        while n!=0:
            m=n%10
            n=n//10
            i+=m
        n=i
        if i<10:
            print("{}".format(n))
            break
