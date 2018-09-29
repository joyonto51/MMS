number=1
count=0
while count<=10:
    number=int(input("Enter a value:"))
    if(number%3==0 or number%5==0):
         print(number)
         count+=1
