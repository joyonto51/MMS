N,B,H,W = map(int, input().split())
List = []
for i in range(H):
    L = []
    P = int(input())
    A = list(map(int,input().split()))
    L.append(P)
    L.append(A)
    List.append(L)

List2 =[]

for j in range(H):
    var1 = List[j]
    l=len(List[j][1])
    v1=0

    for k in range(l):
        var2 = var1[0]
        var3 = var1[1]
        v2 = 0

        for item in var3:

            if item >= N:
                    v2 += 1
            else:
                continue
            print(v2)
            if v2==l*W:
               v1 +=1
            else:
                continue
    print(v1)
    if v1==l:
        List2.append(var1[0])
    else:
        continue

#S = ()
print(List2)



