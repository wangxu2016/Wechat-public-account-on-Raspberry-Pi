# coding:utf-8
# 通过传感器获取温度
# 输出一个数值
import RPi.GPIO as GPIO
import time

channel = 4
data = []
j = 0

GPIO.setmode(GPIO.BCM)

time.sleep(0.1)

GPIO.setup(channel, GPIO.OUT)
GPIO.output(channel, GPIO.LOW)
time.sleep(0.02)
GPIO.output(channel, GPIO.HIGH)
GPIO.setup(channel, GPIO.IN)

while GPIO.input(channel) == GPIO.LOW:
    continue
while GPIO.input(channel) == GPIO.HIGH:
    continue

while j < 40:
    k = 0
    while GPIO.input(channel) == GPIO.LOW:
        continue
    while GPIO.input(channel) == GPIO.HIGH:
        k += 1
        if k > 100:
            break
    if k < 8:
        data.append(0)
    else:
        data.append(1)

    j += 1

temperature_bit = data[16:24]
temperature_point_bit = data[24:32]
check_bit = data[32:40]
temperature = 0
temperature_point = 0

for i in range(8):
    temperature += temperature_bit[i] * 2 ** (7 - i)
    temperature_point += temperature_point_bit[i] * 2 ** (7 - i)

GPIO.cleanup()
print temperature