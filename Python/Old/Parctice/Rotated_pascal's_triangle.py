def rotated_pascal_triangle(n):
    list_1 = []
    for i in range(n):
        list_1.append([])
        list_1[i].append(1)

        for j in range(1,i):
            list_1[i].append(list_1[i-1][j-1] + list_1[i-1][j])
        if i!=0:
            list_1[i].append(1)

    list_2 = []
    for i in range(n):
        list_2.append([])
        for j in range(n + 1):
            try:
                list_2[i].append(list_1[j][i])
            except:
                pass
    sp = n//2
    if sp < 2:
        sp =2
    list_2 = list_2[::-1]
    for i in range(n):
        print((n-i)*(" "*sp),end="")
        for j in range(i+1):
            print("{:{spc}}".format(list_2[i][j],spc=sp),end="")
        print()

rotated_pascal_triangle(3)