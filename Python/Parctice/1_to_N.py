def range_printer(n):
    numbers = ""
    if n > 0:
        for i in range(1, n+1):
            print(i)
            if i==n:
                break
            print(end=", ")

    else:
        for i in range(1, n-1, -1):
            print(i,end =", ")

    print(numbers)
range_printer(5)
range_printer(-3)
