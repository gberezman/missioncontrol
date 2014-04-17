import pygame.mixer
from time import sleep

class Audio:

    def play(self, sound):
        self.getSound( sound ).play()

    def playContinuously(self, sound):
        self.getSound( sound ).play( loops = -1 )

    def stop(self, sound):
        self.getSound( sound ).stop()

    def playES(self, sound):
        self.stopES()
        self.__esChannel.play( self.getSound( sound ) )

    def stopES(self):
        self.__esChannel.stop()

    def playCaution(self, sound = 'caution'):
        self.stopCaution()
        self.__cautionChannel.play( self.getSound( sound ), loops = -1 )

    def stopCaution(self):
        self.__cautionChannel.stop()

    def isCautionPlaying(self):
        return self.__cautionChannel.get_busy()

    def setPlayState(self, sound, isOn):
        if isOn:
            self.play( sound )
        else:
            self.stop( sound )

    def setContinuousPlayState(self, sound, isOn):
        if isOn:
            self.playContinuously( sound )
        else:
            self.stop( sound )

    def isPlaying(self, sound):
        return self.getSound( sound ).get_num_channels() > 0

    def getSound(self, sound):
        return self.sounds.setdefault( sound, self.defaultSound )

    def stopAll(self):
        pygame.mixer.stop()

    def __init__(self):

        pygame.mixer.quit()
        pygame.mixer.init()
        pygame.mixer.set_reserved( 2 )

        self.__cautionChannel = pygame.mixer.Channel( 0 )
        self.__esChannel      = pygame.mixer.Channel( 1 )

        # Should replace this with white noise or blank audio
        self.defaultSound  = pygame.mixer.Sound( 'audio/rocket.wav' )

        self.sounds = {
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
    def __init__(self):
        self.lastFn = None

    def play(self, sound): 
        self.lastFn = 'play'

    def playContinuously(self, sound):
        self.lastFn = 'playContinuously'

    def stop(self, sound):
        self.lastFn = 'stop'

    def playES(self, sound):
        self.lastFn = 'playES'

    def stopES(self):
        self.lastFn = 'stopES'

    def playCaution(self):
        self.lastFn = 'playCaution'

    def stopCaution(self):
        self.lastFn = 'stopCaution'

    def setPlayState(self, sound, isOn):
        self.lastFn = 'setPlayState'

    def setContinuousPlayState(self, sound, isOn):
        self.lastFn = 'setContinuousPlayState'

    def sounds(self):
        return []

if __name__ == '__main__':

    audio = Audio()

    for sound in audio.sounds:
        print "playing {} for at most 1 second".format( sound )
        audio.play( sound )
        sleep( 1 )
        audio.stop( sound )

    print "playing continuously for 2 seconds"
    audio.playContinuously( 'spsThruster' )
    sleep( 2 )
    audio.stop( 'spsThruster' )

    print "playing caution for 2 seconds"
    audio.playCaution()
    sleep( 2 )
    audio.stopCaution()

    print "playing an event sequence for 2 seconds"
    audio.playES( 'ES1' )
    sleep( 2 )
    audio.stopES()

    print "playing dummy sound (should be no audio or error)"
    audio.play( 'missing' )
