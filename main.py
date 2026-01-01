"""
Blynk is a platform with iOS and Android apps to control
Arduino, Raspberry Pi and the likes over the Internet.
You can easily build graphic interfaces for all your
projects by simply dragging and dropping widgets.

  Downloads, docs, tutorials: http://www.blynk.cc
  Sketch generator:           http://examples.blynk.cc
  Blynk community:            http://community.blynk.cc
  Social networks:            http://www.fb.com/blynkapp
                              http://twitter.com/blynk_app
"""
#import library
import BlynkLib
from scripts import wol
from scripts import send_IR
import RPi.GPIO as GPIO
from scripts import temp
from time import sleep
import datetime as d
from dotenv import load_dotenv
import os
import json
from scripts import discord

OUTSIDE_MODE=False
JSONPATH="/home/tyaku/blynk-library-python/main/Settings.json"
load_dotenv()
#set GPIO and key
GPIO.setwarnings(False)       # ・・・ ②
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
BLYNK_AUTH = str(os.getenv("BLYNK_AUTH"))
MAC=str(os.getenv("MAC"))

# Initialize Blynk and server
blynk = BlynkLib.Blynk(BLYNK_AUTH)
last_time = d.datetime.now()
discord.send("Server_booted")
discord.send("This server Disable Outside mode...")
# Register virtual pin handler
@blynk.on("V5")
def v5_write_handler(value):
	global OUTSIDE_MODE
	json_value={"OUTSIDE_MODE":False}
	print(value)
	if value[0]=="1":
		OUTSIDE_MODE=True
		discord.send("This server Enable Outside mode...")
		json_value["OUTSIDE_MODE"]=True

	elif value[0]=="0":
		OUTSIDE_MODE=False
		discord.send("This server Disable Outside mode...")

	with open(JSONPATH,"w") as f:
		json.dump(json_value,f,ensure_ascii=False, indent=4)

@blynk.on("V0")
def v0_write_handler(value):
	"""
	V0 == True　ならば　PCを点ける
	"""
	print(value)
	if(value[0]=="1"):
		wol.wake_on_lan(MAC)
		blynk.virtual_write(10,1)
		sleep(1)
		discord.send("Booting Desktop...")

	elif(value[0]=="3"):
		if OUTSIDE_MODE:
			discord.send("OUTSIDE Mode was Enabled!! You can't do it!!")
			return -1
		send_IR.send_cooler(0)
		blynk.virtual_write(10,1)
		sleep(1)
		discord.send("Stop Cooling...")


@blynk.on("V4")
def v4_write_handler(value):
	if OUTSIDE_MODE:
		discord.send("OUTSIDE Mode was Enabled!! You can't do it!!")
		blynk.virtual_write(4, 0)
		return -1
	sleep(1)
	if(value[0] == "1"):
		send_IR.send_cooler(4)
	elif(value[0] =="2"):
		send_IR.send_cooler(5)
	elif(value[0] =="3"):
		send_IR.send_cooler(6)
	elif(value[0] =="-1"):
		send_IR.send_cooler(1)
	elif(value[0] =="-2"):
		send_IR.send_cooler(2)
	elif(value[0] =="-3"):
		send_IR.send_cooler(3)
	blynk.virtual_write(10,1)
	blynk.virtual_write(4, 0)

def write_temp():
	result=temp.get_temp()

	if(result[0] == 0 and result[1] == 0):
		discord.alert("Sensor Error")
	else:
		unconfort=0.81*result[0]+0.01*result[1]*(0.99*result[0]-14.3)+46.3

		discord.send_temp(f"temperature:{result[0]}")
		discord.send_temp(f"humidity:{result[1]}")
		if(unconfort>80.0):
			discord.alert("Too Unconfortable!!! Open rooms door!!")
		discord.send_temp(f"Unconfortable Index:{unconfort:.2f}")
def main():
	try:
		global last_time
		while True:
			blynk.run()
			sleep(0.5)
	except Exception as e:
		err = str(e)
		discord.alert(err)

if __name__ == "__main__":
	main()
