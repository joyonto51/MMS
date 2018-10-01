import os.path
from os import path
import pathlib

def main():
	# file checking by using path.exists() function
	print("file exists: ", path.exists("guru99.txt"))
	print("file exists: ", path.exists("guru98.txt"))
	# file checking by using path.isfile() function
	print("file isfile?: ", path.isfile("guru99.txt"))
	print("file isfile?: ", path.isfile("guru98.txt"))
	# directory checking by using path.isdir() function
	print("Is it directory?: ", path.isdir("pm"))
	print("Is it directory?: ", path.isdir("guru98.txt"))
	# file checking by using pathlib.Path() function
	file = pathlib.Path("guru99.txt")
	if file.exists():
		print("File exists")
	else:
		print("File not exists")

if __name__ == "__main__":
	main()