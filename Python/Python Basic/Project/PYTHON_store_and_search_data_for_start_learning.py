import subprocess as sp
def add_data(id_,name,phone):
	data = "{:10d}{:60s}{:15s}".format(id_,name,phone)
	print(data)

	file = open('db.txt','a')
	file.write(data)
	file.close()
def get_data():
	students = []
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
		# print("id:",id_,"name:",name,"phone:",phone)
		student = {'name':name, 'id':id_, 'phone':phone}
		students += [student]
	return students

def show_data():
	students = get_data()
	for student in students:
		print(student)

def show_data_by_id(id_):
	students = get_data()
	for student in students:
		#print(student['name'])
		if int(student['id']) == int(id_):
			print(student)
			break
	else:
		print("No data found at roll",id_)

def select():
	sp.call('cls',shell=True)
	sel = input("1. Add data\n 2.Show Data\n 3.Search\n 4.Exit\n\n")

	
	if sel=='1':
		sp.call('cls',shell=True)
		id_ = int(input('id: '))
		name = input('Name: ')
		phone = input('phone: ')
		add_data(id_,name,phone)
	elif sel=='2':
		sp.call('cls',shell=True)
		show_data()
		input("\n\npress enter to back:")
	elif sel=='3':
		sp.call('cls',shell=True)
		id__ = int(input('Enter Id: '))
		show_data_by_id(id__	)
		input("\n\npress enter to back:")
	else:
		return 0;
	return 1;


while(select()):
	pass
