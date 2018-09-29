while True:
	N = int(input())
	if N < 0:
		break
	T = 0
	for i in range(N+1):
		T += i
		
	print(T+1)