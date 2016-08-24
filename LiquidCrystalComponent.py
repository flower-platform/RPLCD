from RPLCD.lcd import CharLCD
from RPLCD import BacklightMode
import RPi.GPIO as GPIO

"""
@flower { isComponent=true }
"""
class LiquidCrystalComponent(CharLCD):
    """
	@flowerChildParameter { ref="pin_rs", defaultValue=15 }
	@flowerChildParameter { ref="pin_rw", defaultValue=18 }
	@flowerChildParameter { ref="pin_e", defaultValue=16 }
    @flowerChildParameter { ref="pin_backlight", defaultValue=None }
    @flowerChildParameter { ref="backlight_enabled", defaultValue=True }
    @flowerChildParameter { ref="cols", defaultValue=16 }
    @flowerChildParameter { ref="rows", defaultValue=2 }
    @flowerChildParameter { ref="dotsize", defaultValue=8 }
    @flowerChildParameter { ref="auto_linebreaks", defaultValue=True }
    """
    def __init__(self, pin_rs, pin_rw, pin_e, d0, d1, d2, d3, d4, d5, d6, d7, pin_backlight, backlight_enabled, cols, rows, dotsize, auto_linebreaks):
        if d4 == 0:
            """
            We're initializing our component using the "4-bit mode".
            Please note that this way, d4, d5, d6, d7 get discarded.
            """
            CharLCD.__init__(self, pin_rs, pin_rw, pin_e, [d0, d1, d2, d3], pin_backlight, BacklightMode.active_low, backlight_enabled, GPIO.BCM, cols, rows, dotsize, auto_linebreaks);
        else:
            """
            We're initializing our component using the "8-bit mode".
            """
            CharLCD.__init__(self, pin_rs, pin_rw, pin_e, [d0, d1, d2, d3, d4, d5, d6, d7], pin_backlight, BacklightMode.active_low, backlight_enabled, GPIO.BCM, cols, rows, dotsize, auto_linebreaks);