while True:
    try:
        A = str(input())
    except:
        break
    C = "AHIMTOUVWXY018"
    B = A[::-1]
    N1, N2, n, n2 = 0, 0, 0, 0
    if A == B:
        N1 = 1
    D = list(A)
    a1= len(A)
    for i in range(a1):
        if D[i] == "L":
            D[i] = "J"
            n += 1
        elif D[i] == "J":
            D[i] = "L"
            n += 1
        elif D[i] == "2":
            D[i] = "S"
            n += 1
        elif D[i] == "S":
            D[i] = "2"
            n += 1
        elif D[i] == "5":
            D[i] = "Z"
            n += 1
        elif D[i] == "Z":
            D[i] = "5"
            n += 1
        elif D[i] == "3":
            D[i] = "E"
            n += 1
        elif D[i] == "E":
            D[i] = "3"
            n += 1
    D = ''.join(D)
    a = D[::-1]
    for j in range(len(a)):
        if a[j] in C:
            n += 1

    if a == A and len(a) == n:
        N2 = 1

    if N1 == 1 and N2 == 1:
        print("{} -- is a mirrored palindrome.\n".format(A))
    elif N1 == 1 and N2 != 1:
        print("{} -- is a regular palindrome.\n".format(A))
    elif N2 == 1 and N1 != 1:
        print("{} -- is a mirrored string.\n".format(A))
    else:
        print("{} -- is not a palindrome.\n".format(A))
