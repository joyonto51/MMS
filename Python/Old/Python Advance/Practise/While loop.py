number=int(input("Enter the number:"))
temp=number
while number>0:
    count=temp
    while count>0:
        print('*',end='')
        count-=1
    print( )
    number-=1
