#encoding: utf-8
import sys
import RPi.GPIO as GPIO

#通过电磁继电器控制灯的开闭

channel = 7
def clean():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # BCM就是我们上面所说的08编号方式。
    GPIO.setup(channel, GPIO.OUT, initial=GPIO.LOW)  # 设置channel=8的接口的编号方式是输出，默认是低电平。

def open():
    GPIO.output(channel, GPIO.HIGH)

def close():
    GPIO.output(channel, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':
    clean()
    if sys.argv[1]=='on':
        open()
        print "灯已打开"
    else:
        close()
        print "灯已关闭"