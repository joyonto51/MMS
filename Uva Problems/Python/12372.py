t = int(input())

for i in range(1,t+1):
    l, w, h = map(int,input().split())

    if (l<=20 and w<=20 and h<=20):
        print("Case {}: good".format(i))
    else:
      print("Case {}: bad".format(i))


