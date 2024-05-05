from machine import Pin, Timer

class ButtonHandler:
    def __init__(self, pin_number, resistor):
        self.button_pin = Pin(pin_number, Pin.IN, resistor)
        self.subscribers_pressed = []
        self.subscribers_released = []
        self.button_pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.debounce_handler)
        self.debounce_timer = Timer()

    def debounce_handler(self, pin):
        self.debounce_timer.init(mode=Timer.ONE_SHOT, period=50, callback=self.notify_subscribers)

    def notify_subscribers(self, timer):
        if self.button_pin.value() == 0:  # Confirm button is still pressed
            for handler, args in self.subscribers_pressed:
                handler(*args)
        else:  # On release
            for handler, args in self.subscribers_released:
                handler(*args)

    def subscribe_pressed(self, handler, *args):
        self.subscribers_pressed.append((handler, args))

    def subscribe_released(self, handler, *args):
        self.subscribers_released.append((handler, args))

    def unsubscribe(self, handler): # Agnostic to the argument provided in the subscribe function. So only checks for method name of subscribed/unubscriber
        self.subscribers_pressed = [(h, args) for h, args in self.subscribers_pressed if h != handler]
        self.subscribers_released = [(h, args) for h, args in self.subscribers_released if h != handler]
