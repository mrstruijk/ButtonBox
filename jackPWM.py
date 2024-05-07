from machine import Pin, PWM

class JackPWM:
    def __init__(self, jack):
        if jack == 'L':  # Left
            self.pins = {
                't': PWM(Pin(3)),  # Green wire
                'r': PWM(Pin(4)),  # White wire
                's': PWM(Pin(2))   # Purple wire
            }
        elif jack == 'R':  # Right
            self.pins = {
                't': PWM(Pin(7)),  # Green wire
                'r': PWM(Pin(8)),  # White wire
                's': PWM(Pin(6))   # Purple wire
            }
        elif jack == 'C':  # USB-C
            self.pins = {
                'plus': PWM(Pin(21)),
                'min': PWM(Pin(22))    # Green wire
            }
        else:
            raise ValueError("Invalid interface type. Choose 'L' (for Left jack), 'R' (for Right jack), or 'C' (for USB-C port).")

    def set_frequency(self, frequency):
        for pwm in self.pins.values():
            pwm.freq(frequency)

    def set_duty_cycle(self, duty, pin_key=None):
        if pin_key:
            if pin_key in self.pins:
                self.pins[pin_key].duty_u16(duty)
            else:
                raise ValueError(f"No pin found with key {pin_key}")
        else:
            for pwm in self.pins.values():
                pwm.duty_u16(duty)

    def on(self):
        # Setting duty cycle to max (assuming 10-bit resolution, max value is 1023)
        self.set_duty_cycle(1023)

    def off(self):
        # Setting duty cycle to 0
        self.set_duty_cycle(0)

    def toggle(self, pin_key):
        # This will toggle the state of a specific pin
        pwm = self.pins[pin_key]
        current_duty = pwm.duty()
        if current_duty > 0:
            pwm.duty(0)
        else:
            pwm.duty(1023)  # Max value for 10-bit

    def cleanup(self):
        # To ensure all PWM are off before exiting
        self.off()

