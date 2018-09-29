T = int(input())
for i in range(1,T+1):
        List1 = list(map(int,input().split()))
        List = List1[1:]
        N=len(List)
        List.sort()
        a = List[int((N-1)/2)]
        print("Case {}: {}".format(i,a))
