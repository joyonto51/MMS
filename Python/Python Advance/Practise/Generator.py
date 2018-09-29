def revrange(n):
    while n >=0:
        yield n
        n = n - 1


for temp in revrange(6):
    print(temp)
