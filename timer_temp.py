
from scripts import discord
from scripts import AHT21
from scripts import BH1750
from datetime import datetime
from figures import headache
from time import sleep
import json

JSONPATH="/home/tyaku/blynk-library-python/main/Settings.json"

def write_temp():
	result=AHT21.get_environmental_data(1)
	result=list(result)
	print(result)
	if(result[0] == 0 and result[1] == 0):
		discord.alert("Sensor Error")
	else:
		print(type(result[1]))
		result[1]+=10
		unconfort=(0.81*result[0])+(0.01*result[1])*(0.99*result[0]-14.3)+46.3
		unconfort=round(unconfort,2)
		sleep(1)
		discord.temp(f"temperature:{result[0]}\nhumidity:{result[1]}\nunconfort index:{unconfort}")
		if(unconfort>80.0):
			sleep(1)
			discord.alert("Too Unconfortable!!! Open rooms door!!")
		if(result[0]<20):
			sleep(1)
			discord.alert("Too Cold!! Turn on your heatings!!")
		if(result[1]<40):
			sleep(1)
			discord.alert("Too Dry!! Humidify your room!!")

	sleep(1)
	AHT21.get_environmental_data(0)

def get_lux():
	now=datetime.now()
	lux=BH1750.check_lux()
	if(lux<200):
		if(7>now.hour and 19<=now.hour):
			discord.alert("Too low lux! Turn On Your lights!")
	elif(lux>=400):
		if(8<=now.hour and 19>=now.hour):
			discord.alert("You forgot Turn off your lights!")

try:
	test=True
	now=datetime.now()
	print(now.hour)
	with open(JSONPATH,"r") as f:
		data=json.load(f)
		print(data)
		if not data["OUTSIDE_MODE"]:
			write_temp()
			if now.hour==11:
				headache.return_today_headache_warn_graph()

except Exception as e:
                err = str(e)
                discord.alert(err)

