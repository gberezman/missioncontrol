import pygame.mixer
from time import sleep

class Audio:

    def __init__(self):
        pygame.mixer.quit()
        pygame.mixer.init( frequency = 48000, buffer = 1024 )

        self.ch0 = pygame.mixer.Channel(0)
        self.ch1 = pygame.mixer.Channel(1)

        quindar  : pygame.mixer.Sound( 'audio/quindar-tone.wav' )
        thruster : pygame.mixer.Sound( 'audio/rocket.wav' )
