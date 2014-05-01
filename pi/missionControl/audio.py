import pygame.mixer

class Audio:

    def play(self, clip, dedicatedChannel = None, continuous = False):
        loops = -1 if continuous else 0
        sound = self.getSound( clip )

        self.stop( sound )

        if dedicatedChannel:
            dedicatedChannel.stop()
            dedicatedChannel.play( sound, loops = loops )
        else:
            sound.play( loops = loops )

        if self.playingClips.count( clip ) == 0:
            self.playingClips.append( clip )

    def stop(self, clip):
        self.getSound( clip ).stop()

        try:
            self.playingClips.remove( clip )
        except ValueError:
            pass

    def togglePlay(self, clip, isOn, dedicatedChannel = None, continuous = False ):
        if isOn:
            self.play( clip, dedicatedChannel, continuous )
        else:
            self.stop( clip )

    def isPlaying(self, clip):
        return self.playingClips.count( clip ) > 0

    def getSoundLabels(self):
        return self.__sounds.keys()

    def getSound(self, clip):
        return self.__sounds.setdefault( clip,  pygame.mixer.Sound( 'audio/silence.wav' ) )

    def stopAll(self):
        pygame.mixer.stop()

    def __init__(self):

        pygame.mixer.quit()
        pygame.mixer.init( frequency = 48000 )
        pygame.mixer.set_reserved( 2 )

        self.cautionChannel       = pygame.mixer.Channel( 0 )
        self.eventSequenceChannel = pygame.mixer.Channel( 1 )

        self.playingClips = []

        self.__sounds = {
            # CONTROL
            'DockingProbeRetract' : pygame.mixer.Sound( 'audio/DockingProbeRetract.wav' ),
            'DockingProbeExtend'  : pygame.mixer.Sound( 'audio/DockingProbeExtend.wav' ),
            'GlycolPump'          : pygame.mixer.Sound( 'audio/glycolPump.wav' ),
            'WasteDump'           : pygame.mixer.Sound( 'audio/wasteDump.wav' ),
            'CabinFan'            : pygame.mixer.Sound( 'audio/cabinFan.wav' ),
            'H2OFlow'             : pygame.mixer.Sound( 'audio/H2OFlow.wav' ),

            # ABORT
            # 'abortPad'
            # 'abortI'
            # 'abortII'
            # 'abortIII'
            # 'abortSIVB'
            'AbortIV'             : pygame.mixer.Sound( 'audio/cantdo.wav' ),

            # BOOSTER 
            'SpsThruster'         : pygame.mixer.Sound( 'audio/rocket.wav' ), # continuous
            #'teiThruster'         : DummySound(), # continuous
            #'tliThruster'         : DummySound(), # continuous
            #'sicThruster'         : DummySound(), # continuous
            #'siiThruster'         : DummySound(), # continuous
            #'sivbThruster'        : DummySound(), # continuous
            #'miThruster'          : DummySound(), # continuous
            #'miiThruster'         : DummySound(), # continuous
            #'miiiThruster'        : DummySound(), # continuous

            # C&WS
            'Caution'             : pygame.mixer.Sound( 'audio/caution.wav' ),

            # CAPCOM
            'Quindarin'           : pygame.mixer.Sound( 'audio/quindar-in.wav' ),
            'Quindarout'          : pygame.mixer.Sound( 'audio/quindar-out.wav' ),

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
            'O2fan'               : pygame.mixer.Sound( 'audio/o2fan.wav' ), # continuous
            'H2fan'               : pygame.mixer.Sound( 'audio/h2fan.wav' ), # continuous
            #'pumps'               : DummySound(), # continuous
            #'heat'                : DummySound(), # continuous

            # PYROTECHNICS
            'CsmDeploy'           : pygame.mixer.Sound( 'audio/csmDeploy.wav' )
        }

if __name__ == '__main__':

    from time import sleep

    audio = Audio()

    for sound in audio.getSoundLabels():
        print "playing {} for at most 1 second".format( sound )
        audio.play( sound )
        sleep( 1 )
        audio.stop( sound )

    print "playing continuously for 2 seconds"
    audio.play( 'SpsThruster', continuous = True )
    sleep( 2 )
    audio.stop( 'SpsThruster' )

    print "playing caution for 2 seconds"
    audio.play( 'caution', dedicatedChannel = audio.cautionChannel, continuous = True )
    sleep( 2 )
    audio.stop( 'caution' )

    print "playing an event sequence for 2 seconds"
    audio.play( 'ES1', dedicatedChannel = audio.eventSequenceChannel )
    sleep( 2 )
    audio.stop( 'ES1' )

    print "playing dummy sound (should be no audio or error)"
    audio.play( 'missing' )