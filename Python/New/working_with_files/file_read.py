try:
	handle = open("test_3.txt", "r")
	for line in handle:
		print(line)
	# while True:
	# 	data = handle.read(1024)
	# 	print(data)

	# 	if not data:
	# 		break

	# with open("test_2.txt") as file_handler:
	# 	for line in file_handler:
	# 		print(line)

except IOError:
	print("An IOError has occurred")

finally:
	handle.close()
