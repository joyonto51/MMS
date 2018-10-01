number=1
count=0
while count<=10:
    number=int(input("Enter a value:"))
    if(number%3 or number%5):
         print(number)
    else:
        count+=1
