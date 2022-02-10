import random
import time
import board
import adafruit_dotstar as dotstar

# Using a DotStar Digital LED Matrix with 64 LEDs connected to digital pins
dots = dotstar.DotStar(board.D13, board.D12, 64, brightness=0.1)  # put at 0.1 when using face shield on robot; 0.05 for testing
# Using a Respeaker 2-Mics Pi Hat with its 3 APA102 LEDs connected to hardware SPI
chest = dotstar.DotStar(board.SCK, board.MOSI, 3, brightness=0.2)


def initialize_pi_hat_leds():
    # a random bright 0 -> 224
    def random_bright():
        return random.randrange(0, 7) * 32

    # MAIN LOOP
    num = 1
    n_chest = len(chest)  # from above assignment
    while num < 10:    # sequence period for flicker
        # Fill each dot with a random bright
        for dot in range(n_chest):
            chest[dot] = (0, 0, random_bright())
        num = num + 1
        time.sleep(.05)     # flicker length
    for dot in range(n_chest):  #resets to solid
        chest[dot] = (0, 0, 255)


def initialize_matrix():
    dots.fill((0, 0, 0))

def initialize_face():
    # Left eye
    dots[49] = (255, 255, 255)
    dots[50] = (255, 255, 255)
    dots[57] = (255, 255, 255)
    dots[58] = (255, 255, 255)
    # Right eye
    dots[53] = (255, 255, 255)
    dots[54] = (255, 255, 255)
    dots[61] = (255, 255, 255)
    dots[62] = (255, 255, 255)
    # Main part of mouth
    dots[18] = (255, 255, 255)
    dots[19] = (255, 255, 255)
    dots[20] = (255, 255, 255)
    dots[21] = (255, 255, 255)
    dots[10] = (255, 255, 255)
    dots[11] = (255, 255, 255)
    dots[12] = (255, 255, 255)
    dots[13] = (255, 255, 255)
    # Neutral expression
    dots[16] = (255, 255, 255)
    dots[17] = (255, 255, 255)
    dots[22] = (255, 255, 255)
    dots[23] = (255, 255, 255)


