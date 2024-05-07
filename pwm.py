from interface import Interface
from machine import Pin, PWM
from time import sleep

class PulseWidthModulation(Interface):
    def __init__(self):
        self.pwm = PWM(Pin(21))
        self.pwm.freq(50)

    # Servo functie
    def setServoCycle(self, position):
        self.pwm.duty_u16(position)
        sleep(0.01)
        
    def step(self):
        while True:
            for pos in range(1000,4500,50):
                self.setServoCycle(pos)
            for pos in range(4500,1000,-50):
                self.setServoCycle(pos)
                
    def shutdown(self):
        pass

# The main execution block should be outside any class definitions
if __name__ == "__main__":
    instance = PulseWidthModulation()
    instance.step()
