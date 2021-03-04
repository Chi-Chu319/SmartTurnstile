import serial




def readSerial():
	# read the serial output
	s = serial.Serial('COM3')

	temp = b''
	while True:
		res = s.read()
		if res == b'\r':
			return temp
		elif res != b' ':
			temp += res



if __name__ == '__main__':
		
	print(readSerial())



# temp = b''
# while True:
# 	try:
# 		res = s.read()
# 		print(str(res))
# 		print(res == b'\r')
# 	except KeyboardInterrupt:
# 		exit()

