Arr = list(map(int, input("Arr = ").split(' ')))

max_value = 0
second_max = 0

for j in Arr:
	if j >= max_value:
		second_max = max_value
		max_value = j
	if j >= second_max and j<max_value:
		second_max = j

print("Ouput = ", max_value*second_max)