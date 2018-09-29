T = int(input())
for i in range(T):
    x,y,z = map(int,input().split())
    a=(x+y)/3
    b= x-a
    c= y-a
    d= z/a
    e= d*b
    if e<0:
        e=0
    elif e%1>0.9:
        e=int(e)+1
    else:
        e=int(e)
    print("{}".format(e))
