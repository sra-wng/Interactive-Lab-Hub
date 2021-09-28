# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Be sure to check the learn guides for more usage information.

This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!

Author(s): Melissa LeBlanc-Williams for Adafruit Industries
"""

import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import
import datetime

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# pylint: disable=line-too-long
# Create the display:
# disp = st7789.ST7789(spi, rotation=90,                            # 2.0" ST7789
# disp = st7789.ST7789(spi, height=240, y_offset=80, rotation=180,  # 1.3", 1.54" ST7789
# disp = st7789.ST7789(spi, rotation=90, width=135, height=240, x_offset=53, y_offset=40, # 1.14" ST7789
# disp = hx8357.HX8357(spi, rotation=180,                           # 3.5" HX8357
# disp = st7735.ST7735R(spi, rotation=90,                           # 1.8" ST7735R
# disp = st7735.ST7735R(spi, rotation=270, height=128, x_offset=2, y_offset=3,   # 1.44" ST7735R
# disp = st7735.ST7735R(spi, rotation=90, bgr=True,                 # 0.96" MiniTFT ST7735R
# disp = ssd1351.SSD1351(spi, rotation=180,                         # 1.5" SSD1351
# disp = ssd1351.SSD1351(spi, height=96, y_offset=32, rotation=180, # 1.27" SSD1351
# disp = ssd1331.SSD1331(spi, rotation=180,                         # 0.96" SSD1331
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)
# pylint: enable=line-too-long

disp.rotation=90

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height

def load_image(filename):
    image = Image.new("RGB", (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    disp.image(image)

    image = Image.open(filename).convert('RGB')
    
    #backlight = digitalio.DigitalInOut(board.D22)
    #backlight.switch_to_output()
    #backlight.value = True


    # Scale the image to the smaller screen dimension
    image_ratio = image.width / image.height
    screen_ratio = width / height
    if screen_ratio < image_ratio:
        scaled_width = image.width * height // image.height
        scaled_height = height
    else:
        scaled_width = width
        scaled_height = image.height * width // image.width
    image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

    # Crop and center the image
    x = scaled_width // 2 - width // 2
    y = scaled_height // 2 - height // 2
    image = image.crop((x, y, x + width, y + height))
    
    return image

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

food_img = load_image("food.jpeg")
walk_img = load_image("walk1.jpeg")
rest_img = load_image("home.jpeg")

while True:
    now = datetime.datetime.now()
    #now = now.replace(hour=9,minute=15,second=0,microsecond=0) # for testing walk
    now = now.replace(hour=8,minute=15,second=0,microsecond=0) # for testing food
    #now = now.replace(hour=8,minute=45,second=0,microsecond=0) # for testing rest
    today8a = now.replace(hour=8,minute=0,second=0,microsecond=0)
    today830a = now.replace(hour=8,minute=30,second=0,microsecond=0)
    today5p = now.replace(hour=17,minute=0,second=0,microsecond=0)
    today530p = now.replace(hour=17,minute=30,second=0,microsecond=0)
    today9a = now.replace(hour=9,minute=0,second=0,microsecond=0)
    today930a = now.replace(hour=9,minute=30,second=0,microsecond=0)
    today1p = now.replace(hour=13,minute=0,second=0,microsecond=0)
    today130p = now.replace(hour=13,minute=30,second=0,microsecond=0)
    today630p = now.replace(hour=18,minute=30,second=0,microsecond=0)
    today730p = now.replace(hour=19,minute=30,second=0,microsecond=0)

    if (((now>today8a) and (now<=today830a)) or ((now>today5p) and (now<=today530p))):
        disp.image(food_img)
    elif (((now>today9a)and(now<=today930a)) or ((now>today1p)and(now<=today130p)) or ((now>today630p)and(now<=today730p))):
        disp.image(walk_img)
    else:
        disp.image(rest_img)
