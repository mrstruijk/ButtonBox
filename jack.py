from machine import Pin

class Jack:
    def __init__(self, jack):
        if jack == 'L':  # Left (ground is brown)
            self.pins = {
                't': Pin(3),  # Green wire
                'r': Pin(4),  # White wire
                's': Pin(2)   # Purple wire
            }
        elif jack == 'R':  # Right (ground is brown)
            self.pins = {
                't': Pin(7),  # Green wire
                'r': Pin(8),  # White wire
                's': Pin(6)   # Purple wire
            }
        elif jack == 'C':  # USB-C (red is 5v, brown is ground)
            self.pins = {
                'plus': Pin(21),  # Orange wire
                'min': Pin(22)    # Green wire
            }
        else:
            raise ValueError("Invalid interface type. Choose 'L' (for Left jack), 'R' (for Right jack), or 'C' (for USB-C port).")

        self.toggle_state = False

    @staticmethod
    def set_pin_mode(pin, mode, pull=None):
        if pull:
            pin.init(mode=mode, pull=pull)
        else:
            pin.init(mode=mode)

    def _read(self, pin, pull=None):
        self.set_pin_mode(pin, Pin.IN, pull)
        return pin.value()

    def _write(self, pin):
        self.set_pin_mode(pin, Pin.OUT)
        pin.on()

    def _off(self, pin):
        self.set_pin_mode(pin, Pin.OUT)
        pin.off()

    def read(self, pull=None):
        results = {k: self._read(v, pull) for k, v in self.pins.items()}
        print(f"Read {self.__class__.__name__}:", results)

    def write(self):
        for pin in self.pins.values():
            self._write(pin)
        print(f"{self.__class__.__name__} on")

    def off(self):
        for pin in self.pins.values():
            self._off(pin)
        print(f"{self.__class__.__name__} off")

    def toggle_write(self):
        if self.toggle_state:
            self.off()
        else:
            self.write()
        self.toggle_state = not self.toggle_state
        return str(self.toggle_state)

    def shutdown(self):
        self.off()