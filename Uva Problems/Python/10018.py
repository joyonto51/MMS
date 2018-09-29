def reverse(n):
    m=0
    while True:
        m += n % 10
        n = n // 10
        if n==0:
            break
        m = m * 10
    return m

T = int(input())
for i in range(T):
    n = int(input())
    x=0
    while True:
        m=reverse(n)
        if x>=1 and n==m:
            break
        n+=m
        x+=1

    print(x,n)
