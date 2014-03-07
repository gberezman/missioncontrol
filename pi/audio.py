import pygame.mixer
from time import sleep

class Audio:

    def __init__(self):
        pygame.mixer.quit()
        pygame.mixer.init( frequency = 48000, buffer = 1024 )

        self.priorityChannel = pygame.mixer.Channel(1)
        self.channel = pygame.mixer.Channel(0)

        self.sounds = {
            'quindar tone' : pygame.mixer.Sound( 'audio/quindar-tone.wav' ),
            'thruster'     : pygame.mixer.Sound( 'audio/rocket.wav' )
        }

def playAll(audio, playChannel):
    for sound in audio.sounds:
        playChannel.play( audio.sounds[sound] )
        while playChannel.get_busy():
            sleep(0.1)

if __name__ == '__main__':
    audio = Audio()

    print "Playing all sounds on regular channel"
    playAll( audio, audio.channel )

    print "Playing all sounds on priority channel"
    playAll( audio, audio.priorityChannel )
