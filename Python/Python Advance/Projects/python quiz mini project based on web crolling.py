'''this is for a simple quiz system using python based on web crolling
 importent link
 request: http://docs.python-requests.org/en/master/
 beautiful soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

 digital ocean tutorial: https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
'''

from bs4 import BeautifulSoup
import requests
import random
import subprocess as sp

def generate_division(division_list, division):
	division_list.remove(division)
	rnd = []
	for i in range(3):
		r = random.randint(0,len(division_list)-1)
		rnd += [division_list[r]]
		division_list.remove(division_list[r])
	return rnd

def generate_ans(division, answer):
	division = generate_division(division,answer)
	position = random.randint(0,3)
	result = division[:position] + [answer] + division[position:]
	return result, position

def quiz():
	gen = generate()
	mark = 0
	for i in range(5):
		tmp = sp.call('clear',shell=True)
		position = random.randint(0,len(gen['district'])-1)
		question = gen['district'][position]
		print('=> What is the division of ',question['name'])
		options, answer = generate_ans(list(gen['division']),question['division'])
		print('1: ',options[0])
		print('2: ',options[1])
		print('3: ',options[2])
		print('4: ',options[3])
		print('\n')
		ans = int(input('Enter answer: '))
		print('\n')
		if ans-1 == answer:
			print("Correct")
			mark += 1
		else:
			print("Wrong, Correct answer is ",answer+1)

		print("Your Point {}/{}".format(mark,i+1))
		input("press Enter to continue")

def generate():
	# get all data
	page = requests.get('https://en.wikipedia.org/wiki/List_of_districts_of_Bangladesh')

	division = []
	district = []
	soup = BeautifulSoup(page.text, 'html.parser')
	f_data = soup.find_all('tr')
	type(f_data)
	for data in f_data:
		td = data.find_all('td')
		if len(td)==5:
			if td[0].string:
				division += [td[2].string]
				district += [{'name':td[0].string, 'division':td[2].string}]

	division = list(set(division))
	return {'district':district, 'division':division}



quiz()
