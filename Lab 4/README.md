# Ph-UI!!!

For lab this week, we focus on both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2021
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the 3 example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python light_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### (Optional) Distance Sensor

Note: We did not distribute this sensor to you, so if you are interested in playing with it, please come pick it up from the TA!

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

<p align="center"> <img src="img/partc_sketches_1.jpg"  width="650" ></p>
<p align="center"> <img src="img/partc_sketches_2.jpg"  width="650" ></p>
<p align="center"> <img src="img/partc_sketches_3.jpg"  width="650" ></p>

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

The sketches raise the question of whether the sensor can be obstructed and still detect proximity, how to make sure the desired action is captured rather than something accidental, how to make a handheld/portable device actually handheld/portable/comfortable to use, where and how the device needs to be positioned to detect the desired signal, how to store the raspberry pi and power pack, and how to manage the aesthetics of the device. I would need to physically prototype placement for the sensor, storage for the device, and the shape and positioning of the device.

**\*\*\*Pick one of these designs to prototype.\*\*\***

I will prototype the handheld color picker device.

### Part D
### Physical considerations for displaying information and housing parts


Here is an Pi with a paper faceplate on it to turn it into a display interface:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibily be mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

<p align="center"> <img src="img/partd_sketches_1.jpg"  width="650" ></p>
<p align="center"> <img src="img/partd_sketches_2.jpg"  width="650" ></p>

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

Some key questions that came up include how to balance the need for a compact size and an ergonomic/comfortable/intuitive shape to hold/use the device, where to place the display to view the output most comfortably, where to place the interactive components, how to make the pi easily removable to make adjustments, and make sure that the weight of the device feels balanced with the pi in it. To understand these, I need to prototype the overall shape of the device, surfaces for the display, and surfaces for the interactive pieces. 

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

I plan to integrate the third display design into my prototype.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

My rationale is that the device should be as compact as possible since it is meant to be a portable, handheld device that someone could use going about their day when they see objects/surfaces with interseting colors. The form will hopefully feel familiar, since I aim to model it after a remote, with the interactive components on the surface of the device and the sensor at the front of the device. The display on the surface should also help users easily see the information picked up from the sensor.

Build a cardbord prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***

Unfolded cardboard prototype:

<p align="center"> 
 <img src="img/proto_open.jpeg"  width="300" >
 <img src="img/proto_open_display.jpeg"  width="300" >
</p>

Folded protoype:

<p align="center"> 
 <img src="img/proto_folded_front.jpeg"  width="300" >
 <img src="img/proto_folded_front_display.jpeg"  width="300" >
</p>
<p align="center"> 
 <img src="img/proto_folded_back.jpeg"  width="300" >
 <img src="img/proto_folded_bottom.jpeg"  width="300" >
 <img src="img/proto_folded_top.jpeg"  width="300" >
</p>

Notes and reflections after making the rough prototype:
- The joystick can be used as both the button for selecting the color and for adjusting the color, so I modified my design to remove the additional button.
- The overall shape and size felt decent, with the front surface about the size of an iPhone. The prototype is deeper to fit the hardware. Weight was also okay, although it felt a little light. The position of the joystick felt natural and easily accessible for my thumb, and the display position seemed reasonable.
- My initial design did not account for the combined height of the sensors/display and the internal pi--I had only considered the pi.
- I also did not consider how to secure the sensors/display. I will need to pay attention to the heights of the various pieces on the sensors/display as well as the heights of the components relative to each other.
- I need to consider where to include a slot for the power cord for the pi, given the orientation I expect the device to be used in and the location of the opening for the power cable on the pi
- My initial design also did not consider the angle with which someone might point the device. The current shape forces the user to have the device perpendicular to the surface they want to find out the color of. I attempted to modify my prototype to have the device be slanted at the top so that the device could be used more naturally. I also attempted to limit the surface area at the top so that it would be obvious which part of the device needed to be pointed at the surface. I had already the cut the coardboard to be too small, so my next iteration will incorporate these improvements

LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which we will be distributing the battery packs in the class. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="Servo_Setup.jpg" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device

#### Part 2 Goals

For part 2, my initial goals for the cardboard protoype were to:
- Account for the combined height of the sensors/display and the internal pi
- Create a way to secure the sensors/display
- Include a slot for the power cord for the pi, given the orientation I expect the device to be used in and the location of the opening for the power cable on the pi
- Update the shape of the device (particularly the top) to make holding the device while trying to sense the color of an item more comfortable. The original design forces the user to hold the device perpendicularly, which strains the wrist. My revision will have the sensor on a slanted surface. The point will also taper to positioning of the device more intuitive.

For the functionality, my goals were to:
- Allow the user to select a sensed color and "lock" the sensor
- Display the selected color and RGB values on the display
- Allow the user to manually edit the selected color

#### First Iteration

To secure the front sensors (oled display, joystick, and LED button), I created a "plate" that I could slide the sensors in and out, and remove/reattach the qwiic connectors easily if I needed to. The below displays the initial design with the joystick and oled display only; the LED button was added later.

<p align="center"> 
    <img src="img/pt2/innerplate/IMG_1836.jpeg"  width="300" >
    <img src="img/pt2/innerplate/IMG_1837.jpeg"  width="300" >
</p>

To experiment with the design of the top of the device, I used notebook paper for a cheaper/easier way to figure out how the cardboard needed to be cut. 

<p align="center"> 
    <img src="img/pt2/devicetop/IMG_1838.jpeg"  width="300" >
    <img src="img/pt2/devicetop/IMG_1839.jpeg"  width="300" >
    <img src="img/pt2/devicetop/IMG_1871.jpg"  width="300" >
</p>

Images of the resulting assembled prototype for this iteration are below. I added a slot for the power cord and included flaps and slots to allow me to easily disassemble and re-assemble the prototype as needed. The design for the top actually ended up being simpler to allow for more flexibility in case I wanted to make changes.

<p align="center"> 
    <img src="img/pt2/int/IMG_1859.jpeg"  width="300" >
    <img src="img/pt2/int/IMG_1860.jpeg"  width="300" >
</p>
<p align="center"> 
    <img src="img/pt2/int/IMG_1861.jpeg"  width="300" >
    <img src="img/pt2/int/IMG_1862.jpeg"  width="300" >
</p>

#### Functionality

The code to run my device is [here](my_color_tool.py). 

*How it Works*

The device starts on "sensing" mode and displays the RGB values of what is being sensed. The user can press the joystick to select or "lock" a sensed color. Once a color is selected, the user can then press the LED button to enter "Edit Mode." The LED light turns on when in Edit Mode. In Edit Mode, the user can toggle between RGB channels by pressing the joystick. The user moves the joystick up or down to increase or decrease the value of the channel. To exit Edit Mode, the user presses the LED button again. The display indicates if changes were made then exits back to the selected color screen. The LED light turns off once Edit Mode has been exited. The RGB values displayed reflect any edits made. From there, the user can either enter Edit Mode again or press the joystick button to go back to sensing mode.

*Changes from the Original Plan*

For the most part, I was able to add the functionality I had planned. However, I was not able to display the selected color on the OLED -- when planning, I had not realized the OLED was monochromatic. Instead of displaying the selected color and the corresponding RGB values, I only displayed the selected RGB values. Similarly, my original plan was to use the joystick to edit the selected color the way one might use the below color picker. I wanted to have the color displayed and RGB values update real-time. Instead, I only displayed the updating RGB values. 

<p align="center"> 
    <img src="img/pt2/color_circle.jpeg"  width="300" >
</p>

Additionally, while coding the interactions to toggle between the different modes, I felt that it would be confusing to have only a single button to switch between the sensing/color selection modes, entering/exiting edit mode, and switching RGB channels while in edit mode. I decided to add in an additional button to toggle edit mode while still using the joystick button for switching between sensing/color selection and switching RGB channels while in edit mode.

#### Final Prototype

Images of my final prototype are included below.

<p align="center"> 
    <img src="img/pt2/final/IMG_1867.jpeg"  width="300" >
    <img src="img/pt2/final/IMG_1868.jpeg"  width="300" >
</p>
<p align="center"> 
    <img src="img/pt2/final/IMG_1869.jpeg"  width="300" >
    <img src="img/pt2/final/IMG_1870.jpeg"  width="300" >
</p>

#### Interaction Videos

Videos of the functionality:
- [Color sensing](https://drive.google.com/file/d/1Y3cx_vUm9MJortihdL2tlWG2VZ9m4Eow/view?usp=sharing)
- [Color selection and editing](https://drive.google.com/file/d/1OfXZY6KUnS7EiPurfARvIxmBseQNDytU/view?usp=sharing)

Video of a user interacting with the device [here](https://drive.google.com/file/d/1aOBTpChue429T9g2xF7KUKpgWZgdfsBw/view?usp=sharing) 

#### Future Work

Given the limitations of the OLED display device used, future work could include using a color display to show the actual sensed colors. Additionally, an improvement on the device could be to save the selected/edited values to a database for later access. Finally, I noticed that the color sensor doesn't seem to work as well when the ambient lighting isn't bright (i.e. it only really works well in the daytime), so I would be interested in further exploring how that could be improved.
