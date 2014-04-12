import pygame.mixer
from time import sleep

class DummySound:

    def play(self, *args):
        pass

    def stop(self, *args):
        pass

class Audio:

    def playES(self, sound):
        self.esChannel.stop()
        self.esChannel.play( sound )

    def playCaution(self, sound):
        self.cautionChannel.stop()
        self.cautionChannel.play( sound )

    def __init__(self):
        pygame.mixer.quit()
        pygame.mixer.init( frequency = 48000, buffer = 1024 )

        pygame.mixer.set_reserved( 2 )
        self.cautionChannel = pygame.mixer.Channel(0)
        self.ESChannel      = pygame.mixer.Channel(1)

        self.sounds = {
            # CONTROL
            'dockingProbeRetract' : DummySound(),
            'dockingProbeExtend'  : DummySound(),
            'glycolPump'          : DummySound(), # continuous
            'SCEPower'            : DummySound(),
            'waste'               : DummySound(),
            'fan'                 : pygame.mixer.Sound( 'audio/cabinFan.wav' ),
            'H2OFlow'             : DummySound(), # continuous
            'intLights'           : DummySound(), # continuous
            'suitComp'            : DummySound(), # continuous

            # ABORT
            'abortPad'            : DummySound(),
            'abortI'              : DummySound(),
            'abortII'             : DummySound(),
            'abortII'             : DummySound(),
            'abortSIVB'           : DummySound(),
            'abortSomething'      : DummySound(),

            # BOOSTER 
            'spsThruster'         : pygame.mixer.Sound( 'audio/rocket.wav' ), # continuous
            'teiThruster'         : DummySound(), # continuous
            'tliThruster'         : DummySound(), # continuous
            'sicThruster'         : DummySound(), # continuous
            'siiThruster'         : DummySound(), # continuous
            'sivbThruster'        : DummySound(), # continuous
            'miThruster'          : DummySound(), # continuous
            'miiThruster'         : DummySound(), # continuous
            'miiiThruster'        : DummySound(), # continuous

            # C&WS

            # CAPCOM
            'quindarin'           : pygame.mixer.Sound( 'audio/quindar-in.wav' ),
            'quindarout'          : pygame.mixer.Sound( 'audio/quindar-out.wav' ),

            # EVENT SEQUENCE
            'ES1'                 : pygame.mixer.Sound( 'audio/ES1.wav' ),
            'ES2'                 : pygame.mixer.Sound( 'audio/ES2.wav' ),
            'ES3'                 : DummySound(),
            'ES4'                 : DummySound(),
            'ES5'                 : DummySound(),
            'ES6'                 : DummySound(),
            'ES7'                 : DummySound(),
            'ES8'                 : DummySound(),
            'ES9'                 : DummySound(),
            'ES10'                : DummySound(),

            # CRYOGENICS
            'o2fan'               : pygame.mixer.Sound( 'audio/o2fan.wav' ), # continuous
            'h2fan'               : pygame.mixer.Sound( 'audio/h2fan.wav' ), # continuous
            'pumps'               : DummySound(), # continuous
            'heat'                : DummySound(), # continuous

            # PYROTECHNICS
            'csmDeploy'           : pygame.mixer.Sound( 'audio/csmDeploy.wav' )
        }

if __name__ == '__main__':

    audio = Audio()
