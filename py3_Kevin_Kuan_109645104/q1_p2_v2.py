# CSE337
# Kevin Kuan
# 109645104
import datetime

try:
    f = open("prices_sample.csv","r")
except FileNotFoundError:
    print("ERROR: prices_sample.csv does not exist!")
    print("Exiting program...")
    exit()

counter=0
my_dict={}
for line in f:
	new_line=line.split(",")
	print(new_line)	
	counter+=1

	#print(float(line[1].rstrip()))
	my_dict[new_line[0]].append((float(new_line[1].rstrip())))

sorted_values=(list(my_dict.values()))
sorted_values.sort()

# print(my_dict["1514934544"])
print("Counter", counter)
print("Size of dictionary",len(my_dict))
mean = sum(sorted_values)/len(sorted_values)
print("Max:", sorted_values[-1], "found at GMT time:", )
print("Min:", sorted_values[0], "found at GMT time:")
print("Mean/Average:", mean)


# newfile = open("test.txt", "w")

# for i in my_dict.keys():
# 	newfile.write(i+"\n")

# newfile.close()
