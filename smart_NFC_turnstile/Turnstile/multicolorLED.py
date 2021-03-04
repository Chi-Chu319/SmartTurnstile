from gpiozero import PWMLED
from time import sleep

class MulticolorLED():
	def __init__(self, R, G, B):
		self.RedLED = PWMLED(R)
		self.GreenLED = PWMLED(G)
		self.BlueLED = PWMLED(B)

	def White(self):
		self.RedLED.value = 1
		self.GreenLED.value = 1
		self.BlueLED.value = 1

	def Green(self):
		self.RedLED.value = 0
		self.GreenLED.value = 1
		self.BlueLED.value = 0

	def Yellow(self):
		self.RedLED.value = 1
		self.GreenLED.value = 1
		self.BlueLED.value = 0

	def Red(self):
		self.RedLED.value = 1
		self.GreenLED.value = 0
		self.BlueLED.value = 0

	def Purple(self):
		self.RedLED.value = 1
		self.GreenLED.value = 0
		self.BlueLED.value = 1

if __name__ == "__main__":
	led = MulticolorLED(21, 20, 16)
	led.Red()
	sleep(3)
	led.Green()
	sleep(3)
	led.White()
	sleep(3)
