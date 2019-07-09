# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

# 通过人体红外传感器判断房间是否有人
# gpio针脚
channel = 16


# 初始化
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.IN)


# 判断是否有人
def detct():
    if GPIO.input(channel) == True:
        print "yes"
    else:
        print 'no'
    GPIO.cleanup()

if __name__ == '__main__':
    time.sleep(1)
    init()
    detct()