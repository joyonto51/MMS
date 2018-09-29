list = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
n = len(list)
list_1 = []
for i in range(n):
    list_1.append([])
    for j in range(n+1):
        try:
            list_1[i].append(list[j][i])
        except:
            pass

    print(list_1[::-1])