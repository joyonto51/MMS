T = int(input())
for i in range(1,T+1):
    N = int(input())
    D = list(map(int,input().split()))
    M = []
    J = []
    mile = 0
    juice = 0
    for j in range(N):
        a = D[j]
        mile += (a//30) + 1
        juice += (a//60) + 1

    mile = mile * 10
    juice = juice * 15


    if mile < juice:
        print("Case {}: Mile {}".format(i,mile))
    elif mile > juice:
        print("Case {}: Juice {}".format(i,juice))
    elif mile == juice:
        print("Case {}: Mile Juice {}".format(i,juice))
