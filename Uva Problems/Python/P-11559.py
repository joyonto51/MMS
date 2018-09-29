N,B,H,W = map(int, input().split())
List = []
for i in range(H):
    L = []
    P = int(input())
    A = list(map(int,input().split()))
    L.append(P)
    L.append(A)
    List.append(L)

List2 = []
for j in range(H):
    var1 = List[j][0]
    v=0
    for k in range(H):

        var2 = List[k][1]
        print(var2)
        if var2[k] >= N:
                print("It's Okay")
                v += 1
                pass
        else:
            print("It's not Okay")
            pass

    if v == W:
            List2.append(var1)
            continue
    else:
        continue

print(List2)
