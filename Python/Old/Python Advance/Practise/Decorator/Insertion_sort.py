A = [3,2,4,5,9,7,8,6,1]
n = len(A)

while True:
    m = 0
    for i in range(1,n):
        j = i-1
        if A[j] > A[i]:
            a = A[j]
            A[j] = A[i]
            A[i] = a
        else:
            m+=1

    if m == n-1:
        break
print(A)