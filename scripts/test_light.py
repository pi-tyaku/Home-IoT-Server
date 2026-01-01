import time
import board
import adafruit_bh1750

i2c = board.I2C()  # SDA/SCL に対応
sensor = adafruit_bh1750.BH1750(i2c)

while True:
    print(f"{sensor.lux:.2f} Lux")
    time.sleep(1)
