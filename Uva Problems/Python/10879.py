N = int(input())
for i in range(1,N+1):
    A,B,C,D =0,0,0,0
    K = int(input())
    for j in range(2,K):
        if K%j==0:
            while A==0:
                A=j
                B=int(K/j)
            if A<j:
                if K%j==0:
                    C=j
                    D=int(K/j)
                    break
    print("Case #{}: {} = {} * {} = {} * {}".format(i,K,A,B,C,D))
