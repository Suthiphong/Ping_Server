#/usr/bin/python
import os
import time
ipaddress = '8.8.8.8'
print('program start')
count = 0
count_ = 0
filelist = './list.txt'


with open(filelist) as f:
	for i in f:
		i = i.rstrip("\n")
		#print(i)
		command = 'ping -c 1 -W 2 '+ i + ' > /dev/null' 	
		result = os.system(command)
		if(result == 0):
			print(i + " [ON]")
			count += 1
		else:
			print(i + " [OFF]")
			count_ += 1

		time.sleep(1)
		
print("Online : " + str(count) + "  Offline : " + str(count_))

