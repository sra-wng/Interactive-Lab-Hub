import time
from adafruit_servokit import ServoKit

def run():
    # Set channels to the number of servo channels on your kit.
    # There are 16 channels on the PCA9685 chip.
    kit = ServoKit(channels=16)

    # Name and set up the servo according to the channel you are using.
    servo0 = kit.servo[0]
    servo1 = kit.servo[4]

    # Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
    # Each servo might be different, you can normally find this information in the servo datasheet
    servo0.set_pulse_width_range(500, 2500)
    servo1.set_pulse_width_range(500, 2500)
 
    try:
        # Set servos to open position
        servo0.angle = 170
        servo1.angle = 0
        time.sleep(.2)
        # Set servos to closed position
        servo0.angle = 80
        servo1.angle = 85
        time.sleep(2)
        
    except KeyboardInterrupt:
        # if interrupted, set servo back to closed position
        servo0.angle = 80
        servo1.angle = 85
        time.sleep(0.5)

if __name__=='__main__':
    run()