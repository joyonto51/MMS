class Employee():

	empcount = 0

	def __init__(self, name , salary):
		self.name = name
		self.salary = salary
		Employee.empcount += 1

	def __del__(self):
		

	def displaycount(self):
		print("Total Employee %d" %Employee.empcount)

	def displayEmployee(self):
		print("Name:", self.name,"Salary: ", self.salary)

emp1 = Employee("Zara",3999)
emp2 = Employee("Manni",42241)

emp1.displayEmployee()
emp2.displayEmployee()

emp1.displaycount()