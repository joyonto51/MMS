T = int(input())
for i in range(1,T+1):
    C = int(input())
    H = list(map(int,input().split()))
    h = 0
    l = 0
    for j in range(C-1):
        a = H[j]
        for k  in range(j+1,j+2):
            b = H[k]
            if a<b:
                h += 1
            elif a==b:
                pass
            elif a>b:
                l += 1
            else:
                pass
    print("Case {}: {} {}".format(i,h,l))




