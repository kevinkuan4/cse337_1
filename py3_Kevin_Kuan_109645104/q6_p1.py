# CSE337
# Kevin Kuan
# 109645104


# lambda function creates a range list
num_list = lambda x,y: range(x,y+1) 

for i in num_list(2,100):
	if i > 1:
		for j in range(2,i):
			if i%j==0:
				break
		else:
			print(i)

