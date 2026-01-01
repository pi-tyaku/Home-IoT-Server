import RPi.GPIO as GPIO
from time import sleep
import dht11
def get_temp():
	# read data using pin 14
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.cleanup()
	instance = dht11.DHT11(pin=14)
	result = instance.read()
	while(1):
		if result.temperature==0 and result.humidity==0:
			print("FAIL TO GET TEMP")
			sleep(1)
			result=instance.read()
		else:
			return [int(result.temperature),int(result.humidity)]
if __name__=="__main__":
	print(get_temp())
