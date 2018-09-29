N=int(input())
n=N//2+1
x=0
for i in range(2,n):
    if N%i==0:
        x=1
        break
    else:
        x=0
if x==1:
    print("Not Prime")
else:
    print("Prime")
