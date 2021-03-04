# The average body temperature varies, from 36.1 to 37.2
# temp over 38 is considered fever
# deprecated, need to be fixed.
import os
import glob
from time import sleep
import os


class TempSensor():
    # TODO fix the temp
    def measureTemperature(self):
    	os.system("sudo ./mlx90614 > output.txt")
    	with open("output.txt", "r") as f:
    		strToMatch = "object temperature = "
    		s1 = f.read()
    		str_start = s1.index(strToMatch)
    		length = len(strToMatch)
    		start_idx = str_start+length
    		temperature = s1[start_idx:start_idx+5]
    		print(temperature)
    		temperature_ = float(temperature)
    	return temperature_

        # return 36.2





if __name__ == '__main__':
	t = TempSensor()
	print(t.measureTemperature())




# class TempSensor:
#     def __init__(self):
#         os.system('modprobe w1-gpio')
#         os.system('modprobe w1-therm')

#         base_dir = '/sys/bus/w1/devices/'
#         device_folder = glob.glob(base_dir + '28*')[0]
#         self.device_file = device_folder + '/w1_slave'
 
#     def read_temp_raw(self):
#         f = open(self.device_file, 'r')
#         lines = f.readlines()
#         f.close()
#         return lines
 
#     def read_temp(self):
#         lines = self.read_temp_raw()
#         while lines[0].strip()[-3:] != 'YES':
#             time.sleep(0.2)
#             lines = read_temp_raw()
#         equals_pos = lines[1].find('t=')
#         if equals_pos != -1:
#             temp_string = lines[1][equals_pos+2:]
#             # offset added to adjust the inaccuracy of the sensor
#             temp_c = float(temp_string) / 1000.0 + 43
#             # temp_f = temp_c * 9.0 / 5.0 + 32.0
#             return temp_c

#     def measure_temp(self):
#         temps = []
#         while True:
#             temp = self.read_temp()
#             if temp >= 36.1:
#                 for i in range(5):
#                     temps.append(self.read_temp())
#                     print(temp)
#                     sleep(0.5)
#                 return sum(temps)/len(temps)
#             print(temp)
#             sleep(0.5)


    
# while True:
#   print(read_temp())  
#   time.sleep(1)
