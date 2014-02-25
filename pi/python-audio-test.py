#!/usr/bin/env python

import pygame.mixer

pygame.mixer.quit()
pygame.mixer.init( frequency = 48000, buffer = 1024 )

quindar = pygame.mixer.Sound( "audio/quindar-tone.wav" )
quindar.set_volume(0.5)
quindarChannel = pygame.mixer.Channel(1)

quindarChannel.play(quindar)
print "playing"
