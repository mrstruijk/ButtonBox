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


class PWMControl(Interface):

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
        self.c_jack.write()
        state = self.c_jack.start_pwm(4500)
        monitor.bool_event("C write " + str(state))

    def left_released(self):
        pass

    def right_pressed(self):
        self.c_jack.write()
        state = self.c_jack.start_pwm(0)
        monitor.bool_event("C " + str(state))

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
            pass  # Handle keyboard interrupt without additional action here
        finally:
            self.shutdown()  # Ensure shutdown is always called when exiting the loop
    
    

    def shutdown(self):
        print("Initiating system shutdown...")
        try:
            self.button_right.unsubscribe(self.right_pressed)
            self.button_right.unsubscribe(self.right_released)
            self.button_left.unsubscribe(self.left_pressed)
            self.button_left.unsubscribe(self.left_released)
            monitor.shutdown()
            led.shutdown()
            self.left_jack.shutdown()
            self.c_jack.shutdown()
            self.right_jack.shutdown()
        except Exception as e:
            print(f"Error during shutdown: {e}")
        finally:
            print("System shutdown completed.")


    

if __name__ == "__main__":
    try:
        _instance = PWMControl()
        _instance.step()
    except KeyboardInterrupt:
        _instance.shutdown()
    except Exception as e:
        print(f"Unhandled exception: {e}")
        if '_instance' in locals():
            _instance.shutdown()