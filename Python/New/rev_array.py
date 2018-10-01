Arr = [0,11,55,88,45,7,9]
ln = (len(Arr)/2)*-1
x = 0
y = 0

def reverse(x,y):
	x-=1
	z = Arr[y]
	Arr[y] = Arr[x]
	Arr[x] = z

	y += 1

	if x>ln:
		reverse(x,y)

reverse(x,y)

print(Arr)
