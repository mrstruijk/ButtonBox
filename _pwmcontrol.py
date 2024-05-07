from interface import Interface
from machine import Pin, Timer
import time

from buttonhandler import ButtonHandler
import joystick
import monitor
from rotary import Rotary
import switches
import led
from jackPWM import JackPWM


class PWMControl(Interface):

    def __init__(self):
        self.left_jack = JackPWM("L")
        self.c_jack = JackPWM("C")
        self.c_jack.set_frequency(50)
        self.right_jack = JackPWM("R")
        self.button_left = ButtonHandler(20, Pin.PULL_UP)  # This one doesn't work with PULL_DOWN
        self.button_right = ButtonHandler(10, Pin.PULL_DOWN)  # This one handles either
        self.rotary = Rotary()
        self.rotary_value = 0
        self.button_right.subscribe_pressed(self.right_pressed)
        self.button_right.subscribe_released(self.right_released)
        self.button_left.subscribe_pressed(self.left_pressed)
        self.button_left.subscribe_released(self.left_released)
        self.rotary.subscribe(self.rotary_changed)
        self.pwm_value = 0
        led.initialize()

    def left_pressed(self):
        state = self.c_jack.set_duty_cycle(2000)
        monitor.bool_event("C write " + str(state))

    def left_released(self):
        pass

    def right_pressed(self):
        state = self.c_jack.set_duty_cycle(4000)
        monitor.bool_event("C " + str(state))

    def right_released(self):
        pass

    def rotary_changed(self, value):
        print(value)
        self.rotary_value = value
        self.pwm_value = 350 * value
        self.c_jack.set_duty_cycle(self.pwm_value)

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