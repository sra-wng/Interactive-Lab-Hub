# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import adafruit_ssd1306
from oled_text import OledText
import time

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
oled_text = OledText(i2c,128,32)

# start with a blank screen
oled.fill(0)
#oled_text.fill(0)
# we just blanked the framebuffer. to push the framebuffer onto the display, we call show()
oled.show()
time.sleep(1)
#oled_text.show()

oled_text.text("Hello", 1) #line 1
oled_text.text ("World", 2) #line 2

oled_text.show()

time.sleep(1)
oled.show()