t = int (input())
for i in range (t):
    f = int (input())
    x=0
    for j in range(f):
        a, b, c = map(int, input().split())
        x1= a*c
        x += x1

    print(x)




