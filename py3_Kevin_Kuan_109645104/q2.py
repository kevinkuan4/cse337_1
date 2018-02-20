# CSE337
# Kevin Kuan
# 109645104

import math

try:
    f = open("prices_sample.csv","r")
except FileNotFoundError:
    print("ERROR: prices_sample.csv does not exist!")
    print("Exiting program...")
    exit()

time = []
values = []

# storing data to time and values lists
for line in f:
	line=line.split(",")
	time.append(float(line[0]))
	values.append(float(line[1].strip()))

n = len(time)
sum_x = sum(time)
sum_y = sum(values)

sum_x_sq = 0 
sum_y_sq = 0
sum_xy = 0
# for x in time:
# 	sum_x_sq += x**2
# for y in values:
# 	sum_y_sq += y**2

# for i in time:
# 	sum_xy

for i in range(len(time)):
	sum_x_sq += (time[i]**2)
	sum_y_sq += (values[i]**2)
	sum_xy += (time[i]*values[i])

top = (sum_xy)-((sum_x*sum_y)/n)
bot =  ((sum_x_sq)-((sum_x**2)/n)) * (((sum_y_sq)-((sum_y**2)/n)))

pearson_coeff =  (top)/(math.sqrt(bot))
print("The Pearson Correlation between the Unix timestamps and bitcoin price is:\n",pearson_coeff)