data=[]
data1=[]
data2=[]
for j in range(5):
    inp=int(input(str(j+1)+"=>"))
    data+=[inp]

for value in data:
    prime=0
    for i in range(2,value):
      if(value%i)==0:
        prime=1
        break
    if(prime==1):
        data1+=[value]
    else:
      data2+=[value]

print("The imprime numbers are:",data1)
print("The prime numbers are:",data2)
