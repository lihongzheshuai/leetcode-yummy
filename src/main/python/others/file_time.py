import datetime
import os, time

file_time = time.localtime(os.stat("/Users/apple/Documents/rkylin/DPS/dps.zip").st_ctime)
y = time.strftime('%Y', file_time)
m = time.strftime('%m', file_time)
d = time.strftime('%d', file_time)
H = time.strftime('%H', file_time)
M = time.strftime('%M', file_time)
file_d_time = datetime.datetime(int(y), int(m), int(d), int(H), int(M))
print(file_time)
t = (file_d_time - datetime.datetime(2018, 1, 31))
print(t.days)
