x=int(input("Enter a value:"))
y=int(input("Enter another value:"))

from my_function import add
print(add(x,y))

import my_function
sum=my_function.add(x,y)
print(sum)
