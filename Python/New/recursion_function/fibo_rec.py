n = int(input())
A = [0,1]
x = n
def fibo(n,x):
	if n>1: 
		A.append(A[-2]+A[-1])
		n-=1
		return fibo(n,x)
	
	return A[x]

print(fibo(n,x))
