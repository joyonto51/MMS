f = open("guru99.txt", "r")
if f.mode == 'r':
	#contents = f.read()
	contents = f.readlines()
	for line in contents:
		print(line)

f.close()
