# CSE337
# Kevin Kuan
# 109645104

def check_file():
	filename = input("Enter the filename: ")
	try:
	    f = open(filename)
	except FileNotFoundError:
	    print("ERROR:", filename,"does not exist!")
	    print("Exiting program...")
	    exit()

	file_parse(f)

def file_parse(file):
	my_dict = {}
	for line in file:
		new_line=line.split()
		print(new_line)
		if str(new_line) in my_dict:
			my_dict[str(new_line)]+=1
		else:
			my_dict[str(new_line)]=1

	return my_dict


if __name__ == "__main__":
	check_file()

