n = int(input())
for i in range(n,0,-1):
    for j in range(i,n):
        print('  ',end='')

    for k in range(1,i*2):
        print('* ',end='')

    print("\n")

for i in range(1,n+1):
    for j in range(i,n):
        print('  ',end='')

    for k in range(1,i*2):
        print('* ',end='')
    print("\n")
