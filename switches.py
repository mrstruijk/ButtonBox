from machine import Pin

# Left
pin_17 = Pin(17, Pin.IN, Pin.PULL_UP)
pin_18 = Pin(18, Pin.IN, Pin.PULL_UP)

# Right
pin_13 = Pin(13, Pin.IN, Pin.PULL_UP)
pin_14 = Pin(14, Pin.IN, Pin.PULL_UP)

def get_left():
    up = pin_17.value()
    down = pin_18.value()
    return get_switch(up, down)


def get_right():
    up = pin_13.value()
    down = pin_14.value()
    return get_switch(up, down)


def get_switch(pin_up, pin_down):
    if pin_up and not pin_down:
        return 1
    elif pin_up and pin_down:
        return 2
    elif not pin_up and pin_down:
        return 3
    else:
        return None


def get_combined():
    if pin_17.value() and not pin_18.value():
        if pin_13.value() and not pin_14.value():
            return 1
        elif pin_13.value() and pin_14.value():
            return 2
        elif not pin_13.value() and pin_14.value():
            return 3
    elif pin_17.value() and pin_18.value():
        if pin_13.value() and not pin_14.value():
            return 6
        elif pin_13.value() and pin_14.value():
            return 5
        elif not pin_13.value() and pin_14.value():
            return 4
    elif not pin_17.value() and pin_18.value():
        if pin_13.value() and not pin_14.value():
            return 7
        elif pin_13.value() and pin_14.value():
            return 8
        elif not pin_13.value() and pin_14.value():
            return 9