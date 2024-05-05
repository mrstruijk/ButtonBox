from interface import Interface
from machine import Pin, Timer
import time

from buttonhandler import ButtonHandler
import joystick
import monitor
from rotary import Rotary
import switches
import led
from jack import Jack

class Combine(Interface):

    def __init__(self):
        self.left_jack = Jack("L")
        self.c_jack = Jack("C")
        self.right_jack = Jack("R")
        self.c_jack.write()
        self.button_left = ButtonHandler(20, Pin.PULL_UP)  # This one doesn't work with PULL_DOWN
        self.button_right = ButtonHandler(10, Pin.PULL_DOWN)  # This one handles either
        self.rotary = Rotary()
        self.rotary_value = 0
        self.button_right.subscribe_pressed(self.right_pressed)
        self.button_right.subscribe_released(self.right_released)
        self.button_left.subscribe_pressed(self.left_pressed)
        self.button_left.subscribe_released(self.left_released)
        self.rotary.subscribe(self.rotary_changed)
        led.initialize()

    def left_pressed(self):
        state = self.left_jack.toggle_write()
        monitor.bool_event("Left write " + state)

    def left_released(self):
        pass

    def right_pressed(self):
        state = self.right_jack.toggle_write()
        monitor.bool_event("(W)right " + state)

    def right_released(self):
        pass

    def rotary_changed(self, value):
        print(value)
        self.rotary_value = value

    def step(self):
        try:
            while True:
                x = joystick.get_x()
                y = joystick.get_y()

                switch = switches.get_combined()
                self.rotary.check_value()
                
                monitor.display(str(x) + " " + str(y), str(switch), str(self.rotary_value))

                time.sleep(0.1)
        except KeyboardInterrupt:
            self.shutdown()
        finally:
            self.shutdown()

    def shutdown(self):
        try:
            self.button_right.unsubscribe(self.right_pressed)
            self.button_right.unsubscribe(self.right_released)
            self.button_left.unsubscribe(self.left_pressed)
            self.button_left.unsubscribe(self.left_released)
            monitor.shutdown()
            led.shutdown()
            self.left_jack.off()
            self.c_jack.off()
            self.right_jack.off()
            print("System shutdown completed.")
        except Exception as e:
            print("Error during shutdown:", e)


# The main execution block should be outside any class definitions
if __name__ == "__main__":
    combine_instance = Combine()
    combine_instance.step()
