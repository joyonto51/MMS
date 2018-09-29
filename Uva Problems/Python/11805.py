T = int(input())
for i in range(1,T+1):
    N,K,P = map(int,input().split())
    a=N-K
    b=P-a
    if a>=P:
        b=K+P
    if b>N:
        b=b%N
    if b==0:
        b=N

    print("Case {}: {}".format(i,b))
