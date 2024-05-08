from machine import Pin, PWM

class JackPWM:
    def __init__(self, jack, freq = 50):
        jack = jack.upper()
        try:
            if jack == 'L':  # Left
                self.pins = {
                    'T': PWM(Pin(3)),  # Green wire
                    'R': PWM(Pin(4)),  # White wire
                    'S': PWM(Pin(2))   # Purple wire
                }
            elif jack == 'R':  # Right
                self.pins = {
                    'T': PWM(Pin(7)),  # Green wire
                    'R': PWM(Pin(8)),  # White wire
                    'S': PWM(Pin(6))   # Purple wire
                }
            elif jack == 'C':  # USB-C
                self.pins = {
                    '+': PWM(Pin(21)),   # Orange wire
                    '-': PWM(Pin(22))    # Green wire
                }
            self.frequency = freq
            self.set_frequency(freq)
        except:
            raise ValueError("Invalid interface type. Choose 'L' (for Left jack), 'R' (for Right jack), or 'C' (for USB-C port).")

    def set_frequency(self, frequency):
        for pwm in self.pins.values():
            pwm.freq(frequency)

    def _duty_from_angle(self, angle):
        duty_cycle = int((angle / 180) * (1000000 / self.frequency) + 2500)
        return duty_cycle

    def set_jack_angle(self, angle):
        duty = self._duty_from_angle(angle)
        for pwm in self.pins.values():
            pwm.duty_u16(duty)

    def set_pin_angle(self, pin_key, angle):
        pin_key = pin_key.upper()
        duty = self._duty_from_angle(angle)
        if pin_key in self.pins:
            self.pins[pin_key].duty_u16(duty)
        else:
            raise ValueError(f"No pin found with key {pin_key}")

    def pin_zero(self, pin_key):
        pin_key = pin_key.upper()
        self.set_pin_angle(pin_key, 0)

    def jack_zero(self):
        # Setting duty cycle to 0
        self.set_jack_angle(0)

    def shutdown(self):
        self.jack_zero()  # To ensure all PWM are off before exiting