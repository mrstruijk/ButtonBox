import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200_000) #Used to be 400_000, but I got some weird errors. Setting it to 100_000 gave different errors. 200_000 works at least for now? (halfway down that chat): https://chat.openai.com/share/199c690a-dd35-40f2-995c-3850d6f35f6d
pixels_x = 128
pixels_y = 64
oled = SSD1306_I2C(pixels_x, pixels_y, i2c)

ROW_ONE = 0
ROW_FINAL = pixels_y - 10
ROW_MIDDLE = ROW_FINAL // 2
ROW_TWO = ROW_FINAL // 3
ROW_THREE = (ROW_FINAL // 3) * 2

DISPLAY_DURATION = 2 # seconds

# State retention dictionary
events = {
    "bool_event": {"timestamp": 0, "message": "", "display_duration": DISPLAY_DURATION}
}

def display(line_one="", line_two="", line_three="", line_four=""):
    try:
        current_time = time.time()
        oled.fill(0)
        oled.text(str(line_one), 0, ROW_ONE)
        oled.text(str(line_two), 0, ROW_TWO)
        oled.text(str(line_three), 0, ROW_THREE)
        if current_time - events["bool_event"]["timestamp"] < events["bool_event"]["display_duration"]:
            oled.text(events["bool_event"]["message"], 0, ROW_FINAL)
        else:
            oled.text(str(line_four), 0, ROW_FINAL)
        oled.show()
    except OSError as e:
        print(f"Failed to update display due to: {e}")

def bool_event(message = ""):
    # Call this method when the button is pressed
    events["bool_event"]["timestamp"] = time.time()
    events["bool_event"]["message"] = message

def clear():
    oled.fill(0)
    oled.show()

def shutdown():
    clear()