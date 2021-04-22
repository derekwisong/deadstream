"""
        sw     gnd
         |      |
     [ROTARY_ENCODER]
       |    |     |
       cl  gnd    dt

"""

import config
import time

from RPi import GPIO
GPIO.setmode(GPIO.BCM)

def setup_knob(cl, dt, sw, name="knob"):
    GPIO.setup(cl, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(dt, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(sw, GPIO.IN, GPIO.PUD_UP)

    def rotate(channel):
        cl_val = GPIO.input(cl)
        dt_val = GPIO.input(dt)
        sw_val = GPIO.input(sw)

        if cl_val == 0 and dt_val == 0:
            direction = ">"
        elif cl_val == 0 and dt_val == 1:
            direction = "<"
        else:
            return
        
        print(f"ROTATE {direction} {name} cl={cl_val} dt={dt_val} sw={sw_val}")
    
    def press(channel):
        cl_val = GPIO.input(cl)
        dt_val = GPIO.input(dt)
        sw_val = GPIO.input(sw)
        if cl_val == 1 and dt_val == 1 and sw_val == 0:
            print(f"PRESS {name} cl={cl_val} dt={dt_val} sw={sw_val}")

    GPIO.add_event_detect(cl, GPIO.FALLING, callback=rotate, bouncetime=50)
    GPIO.add_event_detect(sw, GPIO.FALLING, callback=press, bouncetime=75)

def setup_button(pin, name="button"):
    if pin == 2 or pin == 3:
        # pins 2 and 3 have built in pull up resistors
        GPIO.setup(pin, GPIO.IN)
    else:
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

    def press(channel):
        val = GPIO.input(pin)
        print(f"PRESS {name} btn={val}")
        
    GPIO.add_event_detect(pin, GPIO.RISING, callback=press, bouncetime=250)

if __name__ == "__main__":
    setup_knob(*config.year_pins, name="year")
    setup_knob(*config.month_pins, name="month")
    setup_knob(*config.day_pins, name="day")
    setup_button(config.rewind_pin, name="rewind")
    setup_button(config.play_pause_pin, name="play/pause")
    setup_button(config.stop_pin, name="stop")
    setup_button(config.ffwd_pin, name="ffwd")
    setup_button(config.select_pin, name="select")

    print(f"Listening for control input. Press Ctrl-C to exit.")

    try:
        while True:
            time.sleep(0.001)
    except KeyboardInterrupt:
        pass

    GPIO.cleanup()