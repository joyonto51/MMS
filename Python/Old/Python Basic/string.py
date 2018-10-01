n = int(input())
l = []
for i in range(7):
    s=''
    for j in range(n):
        s+=(7-i)*' '+i*'# '+ (8-i)*' '
    l.append(s)

for item in l:
    print(item)
