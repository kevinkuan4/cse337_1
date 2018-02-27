import re
def password_checker(passwd):
	#(?=.{8,})(?=.*[a-zA-z])(?=.*[0-9])(?=.*\W)
	#if re.search("(?=.{8,})(?=.+[a-zA-z])(?=.+[0-9])(?=.+\W)",passwd) is None:
		#return False
	# checks the len and second condition
	if re.search(".{8,}",passwd) is None:
		print(passwd,"Error: Too short, need to be longer than 8 characters")
		return False
	elif re.search("[0-9]",passwd) is None:
		print(passwd, "Error: No number")
		return False
	elif re.search("[a-zA-Z]",passwd) is None:
		print(passwd,"Error: No alphabet letter")
		return False
	elif re.search("\W",passwd) is None:
		print(passwd,"Error: No special character")
		return False
	
	# Checks for consecutive
	# Also stores characters used in list
	char_used=[]
	prev = ""
	for i in passwd:
		if prev==i:
			print(passwd,"Error: Consecutive characters")
			return False
		else:
			prev=i

		if i not in char_used:
			char_used.append(i)
		
	# Checks ordinal
	for i in range(len(passwd)-2):
		if ord(passwd[i])+1==ord(passwd[i+1]) and ord(passwd[i])+2 == ord(passwd[i+2]):
			print(passwd,"Error: Increasing value issue (ordinal)")
			return False

	# Checks for amount of distinct chars
	if len(char_used) < len(passwd)/2:
		print(passwd, "Error: Not enough distinct characters")
		return False

	print(passwd, "Password is good!")
	return True

	

# (password_checker("ab12Aa!23"))
# (password_checker("a121ab32s"))
# (password_checker("0123aa!@#"))
# (password_checker("absdada!!23"))
# (password_checker("33aszx#!"))
# (password_checker("aaaabb@@@@"))
# (password_checker("$###@!@#$"))
# (password_checker("ab12!"))
# (password_checker("helloooooooo"))
# (password_checker("12345678"))
# (password_checker("helloooooooo"))
# password_checker("1234asz!32")
# password_checker("231acd!#A")
# password_checker("52xyz@!@")
# password_checker("fsax!#123^S")
# password_checker("ab!2!2!2!2")

