Arr = [1,2,4,5,6,8,9,11,13,15,17]
while True:
    try:
        k = int(input())
    except:
        break
    y = 0
    n = 0
    a,b =0, 0

    for item in Arr:
        a =item
        c = k - item

        m = 0
        begin = 1
        end = len(Arr)
        mid = (begin + end) // 2
        while (begin <= end) and (Arr[mid] != c):
            if c < Arr[mid]:
                end = mid - 1
            else:
                begin = mid + 1

            mid = (begin + end) // 2

            if Arr[mid] == c:
                m = mid + 1
                b = Arr[mid]

            else:
                m = -1

        y = m
        n += 1

        if b != 0:
            break


    print(a,b)
    print(n,y)