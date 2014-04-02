import pygame.mixer
from time import sleep

class Audio:

    def __init__(self):
        pygame.mixer.quit()
        pygame.mixer.init( frequency = 48000, buffer = 1024 )

        pygame.mixer.set_reserved( 2 )
        self.cautionChannel = pygame.mixer.Channel(0)
        self.ESChannel      = pygame.mixer.Channel(1)

        self.quindarin   = pygame.mixer.Sound( 'audio/quindar-in.wav' )
        self.quindarout  = pygame.mixer.Sound( 'audio/quindar-out.wav' )
        self.spsThruster = pygame.mixer.Sound( 'audio/rocket.wav' )
        self.fan         = pygame.mixer.Sound( 'audio/cabinFan.wav' )
        self.o2fan       = pygame.mixer.Sound( 'audio/o2fan.wav' )
        self.h2fan       = pygame.mixer.Sound( 'audio/h2fan.wav' )
        self.csmDeploy   = pygame.mixer.Sound( 'audio/csmDeploy.wav' )
        self.ES1         = pygame.mixer.Sound( 'audio/ES1.wav' )
        self.ES2         = pygame.mixer.Sound( 'audio/ES2.wav' )
