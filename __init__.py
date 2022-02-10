# Lidar steered Bioloid robot project
# Used to develop actions for attempt to incorporate into Mycroft Bioloid robot
# Using a laser analog distance sensor - TOF10120

from .Motions import *
from .LEDs import *
from .LIDAR import *


# SETUP FACE
# Using an Adafruit DotStar 8x8 LED Matrix connected to digital pins 12 and 13 to make faces - see actions_leds module
# Initialize face LED-matrix to all off
initialize_matrix()
# Initialize basic neutral face
initialize_face()

min_dist = 10 # inches


# MAIN LOOP
while True:
    forward()
    dist = read_sensor()
    print("Distance to any object is " + dist)

    if dist < 10: # Sees something less than 10 inches in front.

        stop()
        sleep(1)

        back()
        sleep(2)

        right()
        sleep(2)

        stop()
        R = read_sensor()
        print("Right distance is " + R)

        left()
        sleep(4)
        stop()
        L = read_sensor()
        print("Left distance is " + L)

        if L <= R: # If more room right, turn back and go in that direction
            right()
            sleep(4)
            forward()

    else:
        forward() # Move in the left direction