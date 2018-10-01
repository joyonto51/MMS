# coding=utf-8
number = int(input())
list = []
dict = {}
for i in range(1,11):
    sum = number*i
    Sum = "{} * {} = {}".format(number,i,sum)
    list.append(Sum)
    b={'sum{}'.format(i):Sum}
    dict.update(b)

print(list)
print(dict)
