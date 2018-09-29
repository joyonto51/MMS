dict ={}
L,H=map(int,input("Input Boundary L H = ").split())
List2 = []

for x in range(L,H+1):
    y=x
    List = []
    while x !=1:
        if x%2==0:
            x=int(x/2)
            List.append(x)

        else:
            x=int(3*x+1)
            List.append(x)

    dict.update({y:len(List)})
    List2.append(len(List))

print(max(List2))


for key, a in dict.items():
    if a ==max(List2):
        print("\nANSWER=",key)
        break
