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
    V = 0
    for k in range(W):

        var2 = List[j][1]

        if var2[k] >= N:
            V += 1
            pass
        else:
            pass

    if V == W:
        List2.append(List[j][0])
        pass
    else:
        pass


if not List2:
    print("stay home")
else:
    List2.sort()
    x = List2[0]
    X = x*N
    if X <= B:
        print("{}".format(X))
    else:
        print("stay home")
