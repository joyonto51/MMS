a = str(input())
x=a
while True:
    while True:
        d=a[::-1]
        c=d[0:2]
        a=d[-1]+c
        print(a)
        a=a[::-1]
        print(a)
        if a==x:
            break

    if a==x:
        break
