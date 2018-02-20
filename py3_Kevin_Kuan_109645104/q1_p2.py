# CSE337
# Kevin Kuan
# 109645104
import datetime
import math

# checking if file exists
try:
    f = open("prices_sample.csv","r")
except FileNotFoundError:
    print("ERROR: prices_sample.csv does not exist!")
    print("Exiting program...")
    exit()

time_list= []
value_list= []
min_time=0
max_time=0
sorted_list=[]

#stores
max=0.0
min=0.0
sum=0.0
median_time= 0
summation = 0.0
start=True

# reading each line and storing into a list
for line in f:
	line=line.split(",")
	sum+=float(line[1])
	value_list.append(float(line[1]))
	time_list.append(line[0])
	# # check if max
	if (float(line[1]) > float(max)):
		max=(line[1])
		max_time = line[0]

	# check if starting , if starting to read from file we just set min as the first value
	if start == True:
		min = (line[1])
		min_time = line[0]
		start=False
	else:
		if (float(line[1]) < float(min)):
			min = (line[1])
			min_time = line[0]
		

# Calc. mean
num_values = len(value_list)
mean = sum/num_values


# Calc. stdv
for val in value_list:
	summation+=(float(val)-mean)**2
stdv = math.sqrt((summation/len(value_list)))

# Calc. median
for elem in value_list:
	sorted_list.append(float(elem))
sorted_list.sort()
if num_values % 2 == 0:
	med_left = sorted_list[int(num_values/2)]
	med_right = sorted_list[int((num_values+1)/2)]
	med = (med_left + med_right)/2
else:
	med= sorted_list[(num_values+1)/ 2]


med_pos = value_list.index(med)

print("Max:", float(max), "found at GMT time:", datetime.datetime.utcfromtimestamp(float(max_time)))
print("Min:", float(min), "found at GMT time:", datetime.datetime.utcfromtimestamp(float(min_time)))
print("Median:", med, "found at GMT time:",datetime.datetime.utcfromtimestamp(float(time_list[med_pos])) )
print("Average/Mean:",mean)
print("Standard Deviation:", stdv)
