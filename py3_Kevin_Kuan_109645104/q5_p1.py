import re
def password_checker(passwd):
	# if len(passwd) < 8:
	# 	return False
	if re.search(r"{,7}",passwd) == None:
		return False	

	return True


print(password_checker("hello"))

