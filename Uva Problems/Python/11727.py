t = int(input())

for i in range(1,t+1):
    a, b, c = tuple(map(int, input().split()))
    if (a>b and b>c or a<b and b<c):
            print("Case {}: {}".format(i,b))

    elif (b>c and c>a or b<c and c<a):
            print("Case {}: {}".format(i,c))

    elif(c>a and a>b or c<a and a<b):
            print("Case {}: {}".format(i,a))





