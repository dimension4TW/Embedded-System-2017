import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)
gpio.setup(11,gpio.OUT)
gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.OUT)


while True:
    print "state1"
    gpio.output(13,True)
    gpio.output(15,False)
    gpio.output(7,True)
    gpio.output(11,False)
    time.sleep(2)
    print "state2"
    gpio.output(13,False)
    gpio.output(15,True)
    gpio.output(7,False)
    gpio.output(11,True)
    print "state3"
    time.sleep(2)
    gpio.output(13,False)
    gpio.output(15,False)
    gpio.output(7,False)
    gpio.output(11,False)

    time.sleep(2)
    
    
    




