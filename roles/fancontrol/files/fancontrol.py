#
# Copyright <2020> <Valentino Constantinou>
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import re
from time import sleep
import RPi.GPIO as GPIO

pin = 4  # The pin ID, edit here to change it
maxTMP = 47  # The maximum temperature in Celsius after which we trigger the fan
stopTMP = maxTMP - 2  # The temperature to deactivate the fan


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    return ()


def get_cpu_temperature():
    res = os.popen("vcgencmd measure_temp").readline()
    temp = re.findall("\d+\.\d+", res)[0]
    # print("temp is {0}".format(temp))  # Uncomment here for testing
    return temp


def fan_on():
    GPIO.output(pin, True)
    return ()


def fan_off():
    GPIO.output(pin, False)
    return ()


def get_temp():
    cpu_temp = float(get_cpu_temperature())
    if cpu_temp > maxTMP:
        fan_on()
    elif cpu_temp < stopTMP:
        fan_off()
    return ()


try:
    setup()
    while True:
        get_temp()
        sleep(2)  # Read the temperature every 5 sec, increase or decrease this limit if you want
except:
    fan_on()
