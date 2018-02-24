# CSE337
# Kevin Kuan
# 109645104


def file_parse():
	filename = input("Enter the filename: ")
	try:
	    f = open(filename,"r")
	except FileNotFoundError:
	    print("ERROR:", filename,"does not exist!")
	    print("Exiting program...")
	    exit()
	my_dict = {}
	for line in f:
		new_line=line.split()
		for word in new_line:
			
			# punct = "?:!,.;)(\'\""
			
			# Removes punctations before and after the words
			# print(word.lower().rstrip(punct).lstrip(punct))
			if str(word) in my_dict:
				my_dict[str(word)]+=1
			else:
				my_dict[str(word)]=1

	return my_dict


if __name__ == "__main__":
	my_dict = file_parse()
