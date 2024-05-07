from machine import Pin, PWM

class Jack:
    def __init__(self, jack):
        if jack == 'L':
            self.pins = {'t': Pin(3), 'r': Pin(4), 's': Pin(2)}
        elif jack == 'R':
            self.pins = {'t': Pin(7), 'r': Pin(8), 's': Pin(6)}
        elif jack == 'C':
            self.pins = {'plus': Pin(21), 'min': Pin(22)}
        else:
            raise ValueError("Invalid interface type. Choose 'L', 'R', or 'C'.")

        self.pwms = {key: PWM(pin) for key, pin in self.pins.items()}
        self.toggle_state = False

    def set_pin_mode(self, pin, mode, pull=None):
        pin.init(mode=mode, pull=pull)

    def read(self, pull=None):
        results = {k: self.set_pin_mode(v, Pin.IN, pull) or v.value() for k, v in self.pins.items()}
        print(f"Read {self.__class__.__name__}:", results)

    def write(self):
        for pin in self.pins.values():
            self.set_pin_mode(pin, Pin.OUT)
            pin.on()
        print(f"{self.__class__.__name__} on")

    def off(self):
        for pin in self.pins.values():
            self.set_pin_mode(pin, Pin.OUT)
            pin.off()
        print(f"{self.__class__.__name__} off")

    def toggle_write(self):
        if self.toggle_state:
            self.off()
        else:
            self.write()
        self.toggle_state = not self.toggle_state
        return str(self.toggle_state)

    def start_pwm(self, duty_cycle=512, frequency=1000):
        for pwm in self.pwms.values():
            pwm.freq(frequency)
            pwm.duty_u16(duty_cycle)
        print(f"{self.__class__.__name__} PWM started with frequency {frequency}Hz and duty cycle {duty_cycle}")

    def change_pwm_duty(self, duty_cycle):
        for pwm in self.pwms.values():
            pwm.duty_u16(duty_cycle)
        print(f"{self.__class__.__name__} PWM duty cycle changed to {duty_cycle}")

    def stop_pwm(self):
        try:
            for pwm in self.pwms.values():
                pwm.deinit()
            print(f"{self.__class__.__name__} PWM stopped")
        except Exception as e:
            print(f"Failed to stop PWM cleanly: {e}")

    def shutdown(self):
        try:
            self.stop_pwm()
            self.off()
        except Exception as e:
            print(f"Failed to shutdown cleanly: {e}")

