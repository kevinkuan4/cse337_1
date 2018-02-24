# CSE337
# Kevin Kuan
# 109645104
from q4_p1 import *

my_dict = file_parse()

print(my_dict)


output=[]
for keys,items in my_dict:

newfile = open("top10words.txt", "w")
	for 