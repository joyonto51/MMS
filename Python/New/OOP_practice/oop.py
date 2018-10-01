class Vehicle(object):
	"""docstring"""

	def __init__(self, color, doors, tires, vtype):
		"""Constructor"""

		self.color = color
		self.doors = doors
		self.tires = tires
		self.vtype = vtype

	def brake(self,):
		"""Stop the car"""
		return "Braking"

	def drive(self):
		"""
		Drive the car
		"""
		return "I'am driving a %s %s!" % (self.color, self.vtype)

class Car(Vehicle):

	def brake(self):
		return "the car braking slowly"


if __name__ == '__main__':

	car = Car("red", 4, 3, "car")
	print(car.brake(car=23))
	print(car.drive())

