import webbrowser

def main():
	with open("sites.txt") as fobj:
		try:
			for num, url in enumerate(fobj):
				webbrowser.open_new_tab(url.strip())
		except Exeption as e:
			print(e)
 	
	print("\nEnjoy")
if __name__ == '__main__':
	main()			
