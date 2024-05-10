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

def _get(axis):
    mapped = map_value(axis, 350, 65535, -1000, 1000)
    capped = capped_value(mapped)
    rounded = round(capped)
    return rounded

def get_x():
    return _get(x_pin.read_u16())


def get_y():
    return _get(y_pin.read_u16())

