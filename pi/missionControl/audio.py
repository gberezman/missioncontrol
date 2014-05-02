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
        return self.__sounds.setdefault( clip,  pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/silence.wav' ) )

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
            'DockingProbeRetract' : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/DockingProbeRetract.wav' ),
            'DockingProbeExtend'  : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/DockingProbeExtend.wav' ),
            'GlycolPump'          : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/glycolPump.wav' ),
            'WasteDump'           : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/wasteDump.wav' ),
            'CabinFan'            : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/CabinFan.ogg' ),
            'H2OFlow'             : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/H2OFlow.wav' ),

            # ABORT
            # 'abortPad'
            # 'abortI'
            # 'abortII'
            # 'abortIII'
            # 'abortSIVB'
            'AbortIV'             : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/cantdo.wav' ),

            # BOOSTER 
            'spsThruster'         : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/SPS.wav' ),
            'teiThruster'         : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/TEI.wav' ),
            'tliThruster'         : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/TLI.wav' ),
            'sicThruster'         : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/S-IC.wav' ),
            'siiThruster'         : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/S-II.wav' ),
            'sivbThruster'        : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/S-IVB.wav' ),
            'miThruster'          : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/M-I.wav' ),
            'miiThruster'         : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/M-II.wav' ),
            'miiiThruster'        : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/M-III.wav' ),

            # C&WS
            'Caution'             : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/caution.wav' ),

            # CAPCOM
            'Quindarin'           : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/quindar-in.wav' ),
            'Quindarout'          : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/quindar-out.wav' ),

            # EVENT SEQUENCE
            'ES1'                 : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/ES1.wav' ),
            'ES2'                 : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/ES2.wav' ),
            #'ES3'                 : DummySound(),
            #'ES4'                 : DummySound(),
            #'ES5'                 : DummySound(),
            #'ES6'                 : DummySound(),
            #'ES7'                 : DummySound(),
            #'ES8'                 : DummySound(),
            #'ES9'                 : DummySound(),
            #'ES10'                : DummySound(),

            # CRYOGENICS
            'o2fan'               : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/o2fan.wav' ),
            'h2fan'               : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/h2fan.wav' ),
            'pumps'               : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/pumps.wav' ),
            'heat'                : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/heat.wav' ),

            # PYROTECHNICS
            'CsmDeploy'           : pygame.mixer.Sound( '/home/pi/MissionControl/pi/missionControl/audio/csmDeploy.wav' )
        }

        self.__sounds['o2fan'].set_volume( 0.2 )
        self.__sounds['h2fan'].set_volume( 0.05 )
        self.__sounds['pumps'].set_volume( 0.5 )
        self.__sounds['heat'].set_volume( 0.3 )

if __name__ == '__main__':

    from time import sleep

    audio = Audio()

    for sound in audio.getSoundLabels():
        print "playing {} for at most 1 second".format( sound )
        audio.play( sound )
        sleep( 1 )
        audio.stop( sound )

    print "using toggle for 2 seconds"
    audio.togglePlay( 'spsThruster', True, continuous = True )
    sleep( 2 )
    audio.togglePlay( 'spsThruster', False )

    print "playing continuously for 2 seconds"
    audio.play( 'spsThruster', continuous = True )
    sleep( 2 )
    audio.stop( 'spsThruster' )

    print "playing caution for 2 seconds"
    audio.play( 'Caution', dedicatedChannel = audio.cautionChannel, continuous = True )
    sleep( 2 )
    audio.stop( 'Caution' )

    print "playing an event sequence for 2 seconds"
    audio.play( 'ES1', dedicatedChannel = audio.eventSequenceChannel )
    sleep( 2 )
    audio.stop( 'ES1' )

    print "playing dummy sound (should be no audio or error)"
    audio.play( 'missing' )
