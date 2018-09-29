data=[]
sum=0
for i in range(5):
    inp=int(input(str(i+1)+"=>"))
    data+=[inp]
for value in data:
    sum=sum+value
print(sum)
