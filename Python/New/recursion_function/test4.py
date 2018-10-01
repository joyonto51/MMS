N = int(input("input="))
A = []
for i in range(N):
	if i<2:
		A.append(i)
	else:
		A.append(A[i-2]+A[i-1])

print(A[N-1])
