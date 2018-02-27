# CSE337
# Kevin Kuan
# 109645104
from q4_p1 import *
import collections

my_dict = file_parse()



result = collections.Counter(my_dict).most_common(10)
# my_list = []
# for i in result:
# 	for j in i:
# 		my_list.append(str(j))

# my_list=",".join(my_list)

newfile = open("top10words.txt", "w")
# for i in my_list:
# 	

for i in result:
	newfile.write(i[0]+","+str(i[1])+"\n")

newfile.close()