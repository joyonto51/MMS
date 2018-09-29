def add_data(id_, name,phone):
	data = "{:10d}{:60s}{:15s}".format(id_,name,phone)
	print(data)

	file = open('db.txt','a')
	file.write(data)
	file.close()
def get_data():
	file = open('db.txt','r')
	data = file.read()
	file.close()
	# print(data)
	ln = len(data)
	for i in range(int(ln/85)):
		start = i*85
		end = start + 85
		student_info = data[start:end]
		id_ = student_info[0:10].strip()
		name = student_info[10:70].strip()
		phone = student_info[70:85].strip()
		print("id:",id_,"name:",name,"phone:",phone)


	else:
		print("Not found in Database")

