import Adafruit_DHT
import os
import pygame
import time
import sys

class pyscope :
    screen = None;

    def __init__(self):

        "Ininitializes a new pygame screen using the framebuffer"
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print "I'm running under X display = {0}".format(disp_no)

        # Check which frame buffer drivers are available
        drivers = ['directfb', 'fbcon', 'svgalib']
        found = False
        for driver in drivers:
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print 'Driver: {0} failed.'.format(driver)
                continue
            found = True
            break

        if not found:
            raise Exception('No suitable video driver found!')

        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print "Framebuffer size: %d x %d" % (size[0], size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))
        # Initialize font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()
        # Initialize mixer

        #6.3
        pygame.mixer.init()
        pygame.mixer.music.load("lab6.mp3")
        pygame.mixer.music.play(-1)
        while(1):
            self.display()


    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

    def display(self):
        base_temperature = 10
        last_y = 600
        for i in range(200,800):
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            if humidity is not None and temperature is not None:
                print(" Temp= "+ str(temperature))
            else:
                print('Failed to get reading. Try again!')

            current_y = (float(temperature - base_temperature)/20)*600
            pygame.mixer.music.set_volume(float(current_y/600))
            pygame.draw.line(self.screen,(255,0,0),(i,last_y),(i,current_y),1)
            last_y = current_y
            pygame.display.update()
            time.sleep(0.1)



# Create an instance of the PyScope class
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)

scope = pyscope()
scope.display()
time.sleep(10)
