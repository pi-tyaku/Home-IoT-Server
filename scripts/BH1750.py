import board
import adafruit_bh1750
from . import discord
def check_lux():
	i2c = board.I2C()  # SDA/SCL に対応
	sensor = adafruit_bh1750.BH1750(i2c)
	discord.lux(f"{sensor.lux:.2f} Lux")
	return sensor.lux

if __name__=="__main__":
	print(check_lux())
