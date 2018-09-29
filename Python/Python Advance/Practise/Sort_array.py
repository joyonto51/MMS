A=list(map(int,input().split()))

while True:
    B=[]
    a =A[0]
    n=0
    for i in range(1,len(A)):
        b =A[i]

        if a>b:
            B.append(b)

        else:
            B.append(a)
            a=b
            n+=1

    B.append(a)
    print(B)
    A=B

    if n==len(A)-1:
        break

print(A)
