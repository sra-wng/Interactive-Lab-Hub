from __future__ import print_function
from adafruit_apds9960.apds9960 import APDS9960
import adafruit_ssd1306, qwiic_joystick, qwiic_button
import time, board, sys, busio
from oled_text import OledText

#set up display, button, joystick, color sensor
def sensor_setup(): 
    # oled display
    i2c_display = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c_display)
    oled_text = OledText(i2c_display,128,32)
    print("Oled display initialized.")

    # color sensor
    i2c = board.I2C()
    apds = APDS9960(i2c)
    apds.enable_color = True
    print("APDS9960 sensor initialized. Color enabled.")

    # joystick
    myJoystick = qwiic_joystick.QwiicJoystick()
    if myJoystick.connected == False:
        print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        exit()
    myJoystick.begin()
    print("Qwiic Joystick initialized. Firmware Version: %s" % myJoystick.version)

    # button
    myButton = qwiic_button.QwiicButton()
    if myButton.begin() == False:
            print("\nThe Qwiic Button isn't connected to the system. Please check your connection", file=sys.stderr)
    print("Qwiic button ready!")

    return myButton, myJoystick, apds, oled, oled_text

#get color data from sensor
def sense_colors(): 
    r, g, b, c = apds.color_data

    # # wait for color data to be ready
    # while not apds.color_data_ready:
    #     print("Preparing color data")
    #     #time.sleep(0.005)
    
    r = convert_16_to_8_bits(r)
    g = convert_16_to_8_bits(g)
    b = convert_16_to_8_bits(b)
    c = convert_16_to_8_bits(c)

    return r,g,b,c

#convert 16 bit RGB values from color sensor to 8 bit values
def convert_16_to_8_bits(input): 
    output = int(round(input/255, 0))
    return output

#track joystick button press count
def check_joystick_button_status(button_press_count, prev_button_value):
    curr_button_value = myJoystick.button

    #increment the joystick button press count only when the value goes from 1 to 0
    if prev_button_value==1 and curr_button_value==0 and not edit_mode: 
        button_press_count += 1
    else: pass 

    prev_button_value = curr_button_value

    return button_press_count, prev_button_value

#track qwiic button press count to determine whether we are in edit mode
def check_edit_mode_status(edit_button_press_count, prev_edit_button_value): 
    
    curr_edit_button_value = myButton.is_button_pressed()

    if curr_edit_button_value and not prev_edit_button_value:
        edit_button_press_count += 1
    else: pass

    if edit_button_press_count%2==1:
        edit_mode = True
    else:
        edit_mode = False
    
    prev_edit_button_value = curr_edit_button_value

    return edit_mode, edit_button_press_count, prev_edit_button_value

#make edits to individual channel values as long as we are in edit mode
def make_edits(j_press_count, r, g, b, r_edit, g_edit, b_edit, prev_j_button_value):
    
    curr_j_button_value = myJoystick.button
    v_val = myJoystick.vertical
    
    #track joystick press count while in edit mode
    if prev_j_button_value==1 and curr_j_button_value==0:
        j_press_count+=1
    else: pass

    channel=""
    if j_press_count%3==0: #edit r
        channel = "R"
        new, old = r_edit, r
        if v_val==0 and r_edit>0:
            new-=1
        elif v_val==1023 and r_edit<1023:
            new+=1
        r_edit = new
    elif j_press_count%3==1: #edit g
        channel = "G"
        new, old = g_edit, g
        if v_val==0 and g_edit>0:
            new-=1
        elif v_val==1023 and g_edit<1023:
            new+=1
        g_edit = new
    elif j_press_count%3==2: #edit b
        channel = "B"
        new, old = b_edit, b
        if v_val==0 and b_edit>0:
            new-=1
        elif v_val==1023 and b_edit<1023:
            new+=1
        b_edit = new
    
    prev_j_button_value = curr_j_button_value
    
    return channel, new, old, prev_j_button_value, r_edit, g_edit, b_edit, j_press_count

#setup
curr_color, color_locked = (-1,-1,-1), False
button_press_count, prev_button_value = 0,1
edit_button_press_count, edit_mode, prev_edit_button_value = 0, False, False
myButton, myJoystick, apds, oled, oled_text = sensor_setup()
brightness = 1

#start with a blank screen
oled.fill(0) 
oled.show()

while True:  #main loop

    #allow sensing if a color hasn't been selected
    if not color_locked: 
        r,g,b,c = sense_colors()
    
    #keep track of joystick button presses
    button_press_count, prev_button_value = check_joystick_button_status(button_press_count, prev_button_value)
    
    edit_mode_entered = False
    myButton.LED_off()

    # if the joystick button press count is odd, 
    # then lock the selected color and allow edit mode toggling
    if button_press_count%2==1:
        
        color_locked = True
        
        #display the selected color
        if not edit_mode and not edit_mode_entered:
            oled_text.text("Selected Color", 1) #line 1
            oled_text.text("", 2)
            oled_text.text(f"RGB: {r},{g},{b}", 3) #line 3
            oled_text.show()
        
        #check if we should enter edit mode
        edit_mode, edit_button_press_count, prev_edit_button_value = check_edit_mode_status(edit_button_press_count, prev_edit_button_value)

        #edit mode setup
        j_press_count = 0
        prev_j_button_value = 1
        r_edit, g_edit, b_edit = r, g, b
        
        while edit_mode: #edit mode
            myButton.LED_on(brightness)
            edit_mode_entered = True
            
            #allow channel-by-channel manual editing
            channel, new, old, prev_j_button_value, r_edit, g_edit, b_edit, j_press_count = make_edits(j_press_count, r, g, b, r_edit, g_edit, b_edit, prev_j_button_value)
            
            oled_text.text(f"Edit Mode - {channel}", 1)
            oled_text.text(f"New Value:{new}",2) 
            oled_text.text(f"Old Value:{old}", 3) 
        
            edit_mode,edit_button_press_count,prev_edit_button_value = check_edit_mode_status(edit_button_press_count, prev_edit_button_value)

        # determine if edits were actually made
        if r_edit!=r or g_edit!=g or b_edit!=b:
            oled_text.text("Values updated", 1)
            oled_text.text(f"New: {r_edit},{g_edit},{b_edit}",2) 
            oled_text.text(f"Old: {r},{g},{b}", 3) 
            r,g,b = r_edit, g_edit, b_edit
            time.sleep(2)
        elif edit_mode_entered:
            oled_text.text("No edits made", 1)
            oled_text.text("", 2)
            oled_text.text("Exiting...", 3)
            time.sleep(2)
        
        myButton.LED_off()

    # if the joystick button press count is even, then display sensing info
    else:
        color_locked = False
        oled_text.text("Sensing...", 1) #line 1
        oled_text.text("", 2)
        oled_text.text(f"RGB: {r},{g},{b}", 3) #line 3
        oled_text.show()