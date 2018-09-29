A = [2, 3, 1, 4, 6, 7, 8, 5, 9]
ln = len(A)
for i in range(ln):
    min_ = i
    for j in range(i+1, ln):
        if A[min_] >  A[j]:
            min_ = j

    a = A[i]
    A[i] = A[min_]

print(A)
