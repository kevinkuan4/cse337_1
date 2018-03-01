# CSE337
# Kevin Kuan
# 109645104

def count_pattern(str, pattern, replace_str):
	assert len(str) >= len(pattern)
	ord_pattern = 0
	result=""
	for i in pattern:
		ord_pattern+=(ord(pattern[0])-ord(i))
	print(ord_pattern)

	# for i in range(len(str)-(len(pattern)-1)):
	i= 0
	while i < len(str)-(len(pattern)-1):
		temp_str=""
		temp_lst=[]
		temp=0

		for j in range(len(pattern)):
			temp_str+=str[i+j]
			temp+=(ord(str[i])-ord(str[i+j]))
			temp_lst.append(ord(str[i])-ord(str[i+j]))

		# print("temp:",temp)
		# print(temp_str)
		# print(temp_lst)
		# print()
		if temp==ord_pattern:
			i+=len(pattern)-1
			result+=replace_str
			# print("pattern found")

		else:
			result+=str[i]
		i+=1
	return result

#a b c d e f g h i j
#1 2 3 4 5 6 7 8 9 10


if __name__ == '__main__':
	print("orig string shihfdddedaaba")
	print("new string",count_pattern("shihfdddedaaba","xyx","123"))
	print("-----------------------------------")
	print("orig string cdcesa")
	print("new string",count_pattern("cdcesa","xyx","123"))
	print("-----------------------------------")
	print("orig string bacjedf")
	print("new string",count_pattern("bacjedf","bac","213"))
	print("-----------------------------------")
	print("orig string adbadsdgjh")
	print("new string",count_pattern("adbadsdgjh","adb","142"))