import re
def password_checker(passwd):
	# if len(passwd) < 8:
	# 	return False

	# if re.search(".{8,}",passwd) is None:
	# 	return False
	# elif re.search("[0-9]",passwd) is None:
	# 	return False
	# elif re.search("[a-zA-Z]",passwd) is None:
	# 	return False

	#(?=.{8,})([a-zA-z])+([0-9])+(\W)+

	if re.search("(?=.{8,})(?=.*[a-zA-z])(?=.*[0-9])(?=.*\W)",passwd) is None:
		return False
	return True


print(password_checker("ab12Aa!23"))
print(password_checker("0123aa!@#"))
print(password_checker("aaaabb@@@@"))
print(password_checker("$###@!@#$"))
print(password_checker("ab12!"))
print(password_checker("helloooooooo"))
print(password_checker("12345678"))
print(password_checker("helloooooooo"))
