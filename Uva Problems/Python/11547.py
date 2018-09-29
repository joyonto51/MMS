t = int(input())

for i in range(t):

    n = int(input())

    n = (((((n*567)/9)+7492)*235)/47)-498

    if n<0:
        n*= -1

    print("{}".format(int(n/10%10)))
