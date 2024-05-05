from lib_rotary_irq_rp2 import RotaryIRQ
import time

class Rotary:
    def __init__(self):
        starting_val = 0
        self.rotary_encoder = RotaryIRQ(pin_num_dt=11, pin_num_clk=12,
                                        min_val=starting_val, max_val=100,
                                        reverse=True, range_mode=RotaryIRQ.RANGE_UNBOUNDED)
        self.subscribers = []
        self.last_value = self.rotary_encoder.value()

    def check_value(self):
        current_value = self.rotary_encoder.value()
        if current_value != self.last_value:
            self.last_value = current_value
            self.notify_subscribers(current_value)

    def notify_subscribers(self, value):
        for handler in self.subscribers:
            handler(value)

    def subscribe(self, handler):
        if handler not in self.subscribers:
            self.subscribers.append(handler)

    def unsubscribe(self, handler):
        if handler in self.subscribers:
            self.subscribers.remove(handler)
    
    def solo_test(self):
        print("Starting monitoring loop...")
        try:
            while True:
                self.check_value()
                time.sleep(0.1)  # Check every 100 ms
        except KeyboardInterrupt:
            print("Program stopped.")
        except Exception as e:
            print("Error occurred:", e)

# Test the class by initializing it and adding a simple subscriber function.
if __name__ == "__main__":
    def print_change(value):
        print("Value Update:", value)

    rotary = Rotary()
    rotary.subscribe(print_change)
    rotary.solo_test()

