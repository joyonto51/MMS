def factorial(number):
    if number == 0:
        return 1
    else:
        sum = number * factorial(number - 1)
        return sum

number=int(input("please input your number:"))
''' 
  num=number-1
  num1= number
for i in range(num,0,-1):
    sum=num1*i
    print(num1,"*",i,"=",sum)
    num1=sum
'''
print(factorial(number))
