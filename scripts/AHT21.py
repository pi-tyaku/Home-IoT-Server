import sys
import board
import busio
import adafruit_ahtx0
import adafruit_ens160
from time import sleep
from . import discord

def get_environmental_data(value):
	"""
    AHT21とENS160から環境データを取得して返却する。

    Returns:
        dict: {
            'temperature': float (℃),
            'humidity': float (%),
            'tvoc': int (ppb),
            'eco2': int (ppm),
            'aqi': int (1〜5)
        }
	"""
	ALERT=1000
    # I2Cバス初期化
	i2c = busio.I2C(board.SCL, board.SDA)

    # センサー初期化
	aht = adafruit_ahtx0.AHTx0(i2c)
	ens = adafruit_ens160.ENS160(i2c)

    # ENS160を標準モードに設定
	ens.operation_mode = adafruit_ens160.MODE_STANDARD

    # AHT21から温湿度取得
	temperature = round(aht.temperature, 2)
	humidity = round(aht.relative_humidity, 2)

    # ENS160へ補正値を送信（温度: K × 64、湿度: % × 512）
	if value==1:
		print("foo")
		return temperature,humidity
    # センサーデータ安定まで少し待つ
	else:
		print("baa")
		sleep(1)

    # データ取得
		tvoc = ens.TVOC      # ppb
		eco2 = ens.eCO2      # ppm
		aqi = ens.AQI        # 1〜5
		if(int(eco2)>=ALERT):
			discord.alert("To much Co2!! Open your window!!")
			sleep(1)

		discord.air(f"eco2:{eco2}\naqi:{aqi}\ntvoc:{tvoc}")
		sleep(1)
if __name__ == '__main__':
	get_environmental_data(0)
	print(get_environmental_data(1))
