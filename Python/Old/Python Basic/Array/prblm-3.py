data=[]
sum1=0
sum2=0
for i in range(5):
    inp=int(input(str(i+1)+"=>"))
    data+=[inp]
for value in data:
    if(value%2==0):
        sum1=sum1+value
    elif(value%2!=0):
        sum2=sum2+value

print("The sum of Even numbers:",sum1)
print("The sum of Odd numbers:",sum2)
sum=sum2-sum1
print("the sum is:",sum2,"-",sum1,"=",sum)

