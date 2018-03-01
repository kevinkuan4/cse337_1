# CSE337
# Kevin Kuan
# 109645104

import q5_p1

strong_passwd =  False

while strong_passwd == False:
	if q5_p1.password_checker(input("Enter a password: ")):
		strong_passwd = True