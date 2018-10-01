Arr = [1,4,5,2,0,7,3,9,-1,-3,-9,-4,-67]
max_number = Arr[0]

for item in Arr:
	if item < max_number:
		max_number = item	

print(max_number)