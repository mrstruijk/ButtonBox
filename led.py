from machine import Pin

led = Pin("LED", Pin.OUT)

def initialize():
    on()

def on():
    led.on()

def off():
    led._off()

def shutdown():
    led._off()