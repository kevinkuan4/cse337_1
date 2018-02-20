# CSE337
# Kevin Kuan
# 109645104

import datetime
try:
    f = open("prices_sample.csv")
except FileNotFoundError:
    print("ERROR: prices_sample.csv does not exist!")
    print("Exiting program...")
    exit()

newfile = open("datetimes.txt", "w")
for line in f:
    line=line.split(",")
    date_time_display= datetime.datetime.utcfromtimestamp(float(line[0]))
    # print(date_time_display)
    newfile.write(str(date_time_display)+"\n")

f.close()
newfile.close()


# print("Time")
# print(datetime.datetime.utcfromtimestamp(1514934544))
# print(datetime.datetime.utcfromtimestamp(1514934546))
    
# value = datetime.datetime.fromtimestamp(timestamp)
# print(value.strftime('%Y-%m-%d %H:%M:%S'))