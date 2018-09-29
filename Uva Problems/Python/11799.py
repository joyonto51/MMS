T = int(input())
for i in range(1,T+1):
    N = list(map(int,input().split()))
    N.sort()
    a = N[-1]
    print("Case {}: {}".format(i,a))
