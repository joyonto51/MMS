inp=input("Enter a number:");
a= int  (inp)
sum=0
sum=sum+a%10

a=int (a/10)
sum=sum+a%10

a=int (a/10)
sum=sum+(a%10)

print (sum)
