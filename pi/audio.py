import pygame.mixer
from time import sleep

class DummySound:

    def play(self, *args):
        pass

    def stop(self, *args):
        pass

class Audio:

    def play(self, sound):
        self.__getSound(sound).play()

    def playContinuously(self, sound):
        self.__getSound(sound).play(loops = -1)

    def stop(self, sound):
        self.__getSound(sound).stop()

    def playES(self, sound):
        self.stopES()
        self.__esChannel.play( self.__getSound(sound) )

    def stopES(self):
        self.__esChannel.stop()

    def playCaution(self):
        self.__cautionChannel.stop()
        self.__cautionChannel.play( self.__getSound('caution'), loops = -1 )

    def stopCaution(self):
        self.__cautionChannel.stop()

    def sounds(self):
        return self.__sounds.keys()

    def __getSound(self, sound):
        return self.__sounds.get(sound, DummySound())

    def __init__(self):
        pygame.mixer.quit()
        pygame.mixer.init( frequency = 48000, buffer = 1024 )
        pygame.mixer.set_reserved( 2 )

        self.__cautionChannel = pygame.mixer.Channel(0)
        self.__esChannel      = pygame.mixer.Channel(1)

        self.__sounds = {
            # CONTROL
            #'dockingProbeRetract' : DummySound(),
            #'dockingProbeExtend'  : DummySound(),
            #'glycolPump'          : DummySound(), # continuous
            #'SCEPower'            : DummySound(),
            #'waste'               : DummySound(),
            'fan'                 : pygame.mixer.Sound( 'audio/cabinFan.wav' ),
            #'H2OFlow'             : DummySound(), # continuous
            #'intLights'           : DummySound(), # continuous
            #'suitComp'            : DummySound(), # continuous

            # ABORT
            #'abortPad'            : DummySound(),
            #'abortI'              : DummySound(),
            #'abortII'             : DummySound(),
            #'abortII'             : DummySound(),
            #'abortSIVB'           : DummySound(),
            #'abortSomething'      : DummySound(),

            # BOOSTER 
            'spsThruster'         : pygame.mixer.Sound( 'audio/rocket.wav' ), # continuous
            #'teiThruster'         : DummySound(), # continuous
            #'tliThruster'         : DummySound(), # continuous
            #'sicThruster'         : DummySound(), # continuous
            #'siiThruster'         : DummySound(), # continuous
            #'sivbThruster'        : DummySound(), # continuous
            #'miThruster'          : DummySound(), # continuous
            #'miiThruster'         : DummySound(), # continuous
            #'miiiThruster'        : DummySound(), # continuous

            # C&WS
            'caution'             : pygame.mixer.Sound( 'audio/caution.wav' ),

            # CAPCOM
            'quindarin'           : pygame.mixer.Sound( 'audio/quindar-in.wav' ),
            'quindarout'          : pygame.mixer.Sound( 'audio/quindar-out.wav' ),

            # EVENT SEQUENCE
            'ES1'                 : pygame.mixer.Sound( 'audio/ES1.wav' ),
            'ES2'                 : pygame.mixer.Sound( 'audio/ES2.wav' ),
            #'ES3'                 : DummySound(),
            #'ES4'                 : DummySound(),
            #'ES5'                 : DummySound(),
            #'ES6'                 : DummySound(),
            #'ES7'                 : DummySound(),
            #'ES8'                 : DummySound(),
            #'ES9'                 : DummySound(),
            #'ES10'                : DummySound(),

            # CRYOGENICS
            'o2fan'               : pygame.mixer.Sound( 'audio/o2fan.wav' ), # continuous
            'h2fan'               : pygame.mixer.Sound( 'audio/h2fan.wav' ), # continuous
            #'pumps'               : DummySound(), # continuous
            #'heat'                : DummySound(), # continuous

            # PYROTECHNICS
            'csmDeploy'           : pygame.mixer.Sound( 'audio/csmDeploy.wav' )
        }

class StubbedAudio:
    def play(self, sound): pass
    def playContinuously(self, sound): pass
    def stop(self, sound): pass
    def playES(self, sound): pass
    def stopES(self): pass
    def playCaution(self): pass
    def stopCaution(self): pass
    def sounds(self): pass

if __name__ == '__main__':

    audio = Audio()

    for sound in audio.sounds():
        print "playing {} for at most 1 second".format(sound)
        audio.play( sound )
        sleep( 1 )
        audio.stop( sound )

    print "playing continuously for 2 seconds"
    audio.playContinuously( 'spsThruster' )
    sleep(2)
    audio.stop( 'spsThruster' )

    print "playing caution for 2 seconds"
    audio.playCaution()
    sleep(2)
    audio.stopCaution()

    print "playing an event sequence for 2 seconds"
    audio.playES( 'ES1' )
    sleep(2)
    audio.stopES()

    print "playing dummy sound (should be no audio or error)"
    audio.play( 'missing' )
