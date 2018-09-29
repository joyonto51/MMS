my_list = [1,2,3,4,7,8,9,11,13,15,20,21,23,25,28,30,33,37,40,45,67]

number = int(input("Enter a number:"))
first =  0
last = len(my_list)-1
found = False
cycle = 0

while first<=last and not found:
    midpoint = (first + last)//2

    if my_list[midpoint]==number:
        found = True

    else:
        if number <= my_list[midpoint]:
            last = midpoint-1

        else:
            first = midpoint+1
    cycle += 1


print('Found afer',cycle,'cycle')