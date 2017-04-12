import math
from pathlib import Path

def area_total_surface(radius, height):
	return 2 * (math.pi * radius * height) + 2 * (math.pi * radius**2)

def get_file():
	fname=''
	while not (fname): fname = input("Enter the data filename: ")
	return fname

def check_file(fname):
	return Path(fname)

def confirm_file():
	fname = get_file()
	is_file = check_file(fname)

	#check if the file exists. if it doesn't display error message
	#then ask the user to enter another filename
	while not (is_file.exists()):
		print (fname + ' is not valid!')
		fname = get_file()
		is_file = check_file(fname)

	return fname

def print_headings():
	print()
	print("Radius	Height	Surface Area")
	print("------	------	------------")

def get_answer():
	
	return input("Continue? [y/n]: ")

def print_out(radius, height, surface_area):	
	print(str(radius) + '\t' + str(height.replace("\n","")) + '\t%.2f' % surface_area)

def goodbye():
	print()
	print("Alez! Tata! Lukim yu!")
	
def main():
	ans = get_answer()
	
	while (ans=='y') or (ans=='Y'):
		fname = confirm_file()

		infile = open(fname, "r")

		#print the headings
		print_headings()

		for line in infile:
			radius, height = line.split(" ")
	
			surface_area = area_total_surface(float(radius), float(height))

			print_out(radius, height, surface_area)
		
		ans = get_answer()

	goodbye()


main()
