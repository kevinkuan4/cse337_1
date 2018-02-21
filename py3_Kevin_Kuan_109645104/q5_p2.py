import q5_p1

strong_passwd =  False

while strong_passwd == False:
	if password_checker(input("Enter a password: ")):
		print("Password is good!")
		strong_passwd = True