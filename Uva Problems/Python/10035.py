while True:
    a,b = map(str,input().split())
    if int(a)==0 and int(b)==0:
        break
    N = 0
    ln1=len(a)
    ln2=len(b)
    m=str(a[::-1])
    n=str(b[::-1])
    x = 0
    y = 0
    w = 0
    z = 0
    c = 0
    while True:
        w+=1
        if ln1>=w:
            for i in range(z,w):
                x = int(m[i])
        else:
            x = 0
            pass
        if ln2>=w:
            for i in range(z,w):
                y = int(n[i])
        else:
            y = 0
            pass
        X = (x+y+c)
        if X>=10:
            N+=1
            c=1
        else:
            c=0
        if w>=ln1 and w>=ln2:
            break
        z+=1

    if N==0:
        print("No carry operation.")
    elif N==1:
        print("{} carry operation.".format(N))
    else:
        print("{} carry operations.".format(N))
