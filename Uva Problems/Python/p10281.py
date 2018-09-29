def get_time(x, y=None):
	h, m, s = map(int, x.split(':'))
	h, m = h*60*60, m*60
	total = h + m + s

	if y:
		y = int(y)
	return total, y

time_ = 0
while True:
	try:
		t = input()
	except:
		break

	if len(t.split()) > 1:
			string_time, speed = t.split()
			time_, speed = get_time(string_time, speed)
	else:
		time_ = get_time(t)
