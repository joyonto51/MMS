#open a file for writing and create it if doesn't exist
f = open("guru99.txt", "a+")

#write some lines of data to the file
for i in range(10,20):
	f.write("This is line %d\r\n" %i)
f.close()

with open("guru99.txt") as file:
	for line in file:
		print(line)
