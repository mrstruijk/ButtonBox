from machine import Pin, ADC
from buttonhandler import ButtonHandler

x_pin = ADC(Pin(26))
y_pin = ADC(Pin(27))

def map_value(value, old_min, old_max, new_min, new_max):
    return new_min + (value - old_min) * (new_max - new_min) / (old_max - old_min)

def capped_value(value):
    if value < -1000:
        value = -1000
    elif -25 < value < 25:
        value = 0
    elif value > 1000:
        value = 1000
    return value

def get_x():
    x_axis = x_pin.read_u16()
    mapped_x = map_value(x_axis, 350, 65535, -1000, 1000)
    capped_x = capped_value(mapped_x)
    rounded_x = round(capped_x)
    return rounded_x

def get_y():
    y_axis = y_pin.read_u16()
    mapped_y = map_value(y_axis, 350, 65535, -1000, 1000)
    capped_y = capped_value(mapped_y)
    rounded_y = round(capped_y)
    return rounded_y