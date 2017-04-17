import os
import pygame
import time

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
        while(1):
            self.display()


    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

    def display(self):
        self.screen.fill(255,0,0)
        pygame.display.update()
        time.sleep(3)
        self.screen.fill(0,255,0)
        pygame.display.update()
        time.sleep(3)
        self.screen.fill(0,0,255)
        pygame.display.update()
        time.sleep(3)


# Create an instance of the PyScope class
scope = pyscope()
scope.display()
time.sleep(10)
