def Ackermann(L,H):
    Dict = {}
    List1 = []
    List3 = []
    for x in range(L,H+1):
        List2 = []
        y = x
        while True:
            if x%2==0:
                x = x/2
                List2.append(x)
            else:
                x = int(3*x+1)
                List2.append(x)
            if x<=1:
                break
        List1.append(len(List2))
        Dict.update({y:len(List2)})
    S = max(List1)

    for key,a in Dict.items():
        if a ==max(List1):
           List3.append(key)
    V = min(List3)
    print("Between {} and {}, {} generates the longest sequence of {} values.".format(L,H,V,S))

while True:
    L,H = map(int,input().split())
    if L==0 and H==0:
        break
    Ackermann(L,H)

