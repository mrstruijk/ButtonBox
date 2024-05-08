from machine import Pin

led = Pin("LED", Pin.OUT)

def initialize():
    turn_on()

def turn_on():
    led.on()

def turn_off():
    led.off()

def shutdown():
    led.jack_zero()