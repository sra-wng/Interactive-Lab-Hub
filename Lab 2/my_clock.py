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
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import
import datetime
import time

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

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

def draw_progress_bar(num_hours, start_time, curr_time):
    # draw progress bar background
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)# Get drawing object to draw on image.
    draw.rectangle([(0,0),(width,height)],fill="grey",outline="grey",width=5)
    disp.image(image)

    steps_needed = datetime.timedelta(hours=num_hours).total_seconds()
    current_step = (curr_time - start_time).total_seconds()

    
    while ((current_step <= steps_needed) and (buttonB.value and not buttonA.value)):
        #draw progress bar
        draw.rectangle([(0,0),(width,height)],fill="#d1d1d1",outline="#d1d1d1",width=5)
        scaled_width = (current_step/steps_needed)*(width-10)
        draw.rectangle([(5,5),(scaled_width+5,height-5)],fill="white")

        #overlay with the current time
        #clock = time.strftime("%H:%M:%S") #use actual time
        clock = curr_time.strftime("%H:%M:%S") #use given time
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
        draw.text((5,height-55), clock, font=font, fill="#1e43fc")
    
        disp.image(image)

        current_step += 1
        curr_time = curr_time + datetime.timedelta(seconds=1) #increment manually for given time
        time.sleep(1)

def add_text(text_1="", text_2=""):
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)# Get drawing object to draw on image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))# Draw a black filled box to clear the image.
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
    draw.text((10, 10), text_1, font=font, fill="#FFFFFF")
    draw.text((10, 50), text_2, font=font, fill="#FFFFFF")
    disp.image(image)

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

food_img = load_image("food.jpeg")
walk_img = load_image("walk1.jpeg")
rest_img = load_image("home.jpeg")

while True:
    now = datetime.datetime.now()
    #now = now.replace(hour=9,minute=15,second=0,microsecond=0) # for testing walk
    #now = now.replace(hour=8,minute=15,second=0,microsecond=0) # for testing food
    #now = now.replace(hour=8,minute=45,second=0,microsecond=0) # for testing rest1
    #now = now.replace(hour=14,minute=45,second=0,microsecond=0) # for testing rest2
    #now = now.replace(hour=23,minute=45,second=0,microsecond=0) # for testing rest3
    today8a = now.replace(hour=8,minute=0,second=0,microsecond=0)
    today830a = now.replace(hour=8,minute=30,second=0,microsecond=0)
    today5p = now.replace(hour=17,minute=0,second=0,microsecond=0)
    today530p = now.replace(hour=17,minute=30,second=0,microsecond=0)
    today9a = now.replace(hour=9,minute=0,second=0,microsecond=0)
    today930a = now.replace(hour=9,minute=30,second=0,microsecond=0)
    today1p = now.replace(hour=13,minute=0,second=0,microsecond=0)
    today130p = now.replace(hour=13,minute=30,second=0,microsecond=0)
    today6p = now.replace(hour=18,minute=0,second=0,microsecond=0)
    today630p = now.replace(hour=18,minute=30,second=0,microsecond=0)
    
    if not buttonA.value and not buttonB.value:  # both pressed
        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)# Get drawing object to draw on image.
        draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))# Draw a black filled box to clear the image.
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
        draw.text((10, 10), "daily schedule", font=font, fill="#FFFFFF")
        draw.text((10, 40), " 8-8:30a food // 8:30-9a rest", font=font, fill="#FFFFFF")
        draw.text((10, 55), " 9-9:30a walk // 9:30-1p rest", font=font, fill="#FFFFFF")
        draw.text((10, 70), " 1-1:30p walk // 1:30-5p rest", font=font, fill="#FFFFFF")
        draw.text((10, 85), " 5-5:30p food // 5:30-6p rest", font=font, fill="#FFFFFF")
        draw.text((10, 100), " 6-6:30p walk // 6:30p+ rest", font=font, fill="#FFFFFF")
        disp.image(image)   

    if (((now>today8a) and (now<=today830a)) or ((now>today5p) and (now<=today530p))):
        if buttonA.value and buttonB.value:  # none pressed
            disp.image(food_img)
        if buttonB.value and not buttonA.value:  # just button A pressed
            #display progress bar
            if ((now>today8a) and (now<=today830a)):
                draw_progress_bar(start_time=today8a, curr_time=now, num_hours=0.5)
            else:
                draw_progress_bar(start_time=today5p, curr_time=now, num_hours=0.5)
        if buttonA.value and not buttonB.value:  # just button B pressed
            #display text
            add_text(text_1 = "food time!", text_2 = "1/4 cup kibble")

    elif (((now>today9a)and(now<=today930a)) or ((now>today1p)and(now<=today130p)) or ((now>today6p)and(now<=today630p))):
        if buttonA.value and buttonB.value:  # none pressed
            disp.image(walk_img)
        if buttonB.value and not buttonA.value:  # just button A pressed
            #display progress bar
            if ((now>today9a)and(now<=today930a)):
                draw_progress_bar(start_time=today9a, curr_time=now, num_hours=0.5)
            elif ((now>today1p)and(now<=today130p)):
                draw_progress_bar(start_time=today1p, curr_time=now, num_hours=0.5)
            else:
                draw_progress_bar(start_time=today6p, curr_time=now, num_hours=0.5)
        if buttonA.value and not buttonB.value:  # just button B pressed
            #display text
            add_text(text_1 = "walkies!", text_2 = "play fetch")

    elif (((now>today830a) and (now<=today9a)) or ((now>today530p) and (now<=today6p))):
        if buttonA.value and buttonB.value:  # none pressed
            disp.image(rest_img)
        if buttonB.value and not buttonA.value:  # just button A pressed      
            if ((now>today830a) and (now<=today9a)):
                draw_progress_bar(start_time=today830a, curr_time=now, num_hours=0.5)
            else:
                draw_progress_bar(start_time=today530p, curr_time=now, num_hours=0.5)
        if buttonA.value and not buttonB.value:  # just button B pressed
            #display text
            add_text(text_1 = "rest & digest")

    else:
        if buttonA.value and buttonB.value:  # none pressed
            disp.image(rest_img)
        if buttonB.value and not buttonA.value:  # just button A pressed 
            if ((now>today930a) and (now<=today1p)): 
                draw_progress_bar(start_time=today930a, curr_time=now, num_hours=3.5)
            elif ((now>today130p) and (now<=today5p)):
                draw_progress_bar(start_time=today130p, curr_time=now, num_hours=3.5)
            else:
                draw_progress_bar(start_time=today6p, curr_time=now, num_hours=14)
        if buttonA.value and not buttonB.value:  # just button B pressed
            if (((now>today930a) and (now<=today1p)) or ((now>today130p) and (now<=today5p))): 
                add_text(text_1 = "let's just nap", text_2 = "and chill")
            else:
                add_text(text_1 = "bed time!", text_2 = "sweet dreams")