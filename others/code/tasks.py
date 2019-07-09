# coding:utf-8
# !/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys
from celery import Celery

# 控制步进电机的正反转
# 由于控制时间比较长增加了异步任务

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/1')  # 配置好celery的backend和broker


def setStep(w1, w2, w3, w4):
    IN1 = 11  # pin11
    IN2 = 12
    IN3 = 13
    IN4 = 15
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)


def stop():
    setStep(0, 0, 0, 0)


@app.task
def forward(delay, steps):
    setup()
    for i in range(0, steps):
        setStep(1, 0, 0, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 0, 0, 1)
        time.sleep(delay)
    destroy()


@app.task
def backward(delay, steps):
    setup()
    for i in range(0, steps):
        setStep(0, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 0)
        time.sleep(delay)
        setStep(1, 0, 0, 0)
        time.sleep(delay)
    destroy()


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    IN1 = 11
    IN2 = 12
    IN3 = 13
    IN4 = 15

    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    action = sys.argv[1].strip()
    if action == 'on':
        backward.delay(0.003, 512)
        print('步进电机正转')
    else:
        forward.delay(0.005, 512)
        print('反转')
