N = int(input())
print("Lumberjacks:")
for i in range(N):
    P = list(map(int,input().split()))
    SL = 0
    LS = 0
    for j in range(9):
        a = P[j]
        for k in range(j+1,j+2):
            b = P[k]
            if a>b:
                LS += 1
            elif a<b:
                SL += 1
            else:
                pass

    if SL==9 or LS==9:
        print("Ordered")
    else:
        print("Unordered")
