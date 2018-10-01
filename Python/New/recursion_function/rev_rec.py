x = 5436
y = 0

def reverse(x,y):
	if x==0:
		return y
	z = x%10
	x = int(x/10)
	y = (y*10)+z
	
	return reverse(x,y)

print(reverse(x,y))