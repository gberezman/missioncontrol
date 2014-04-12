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

        # CONTROL
        self.dockingProbeRetract = DummySound()
        self.dockingProbeExtend  = DummySound()
        self.glycolPump          = DummySound() # continuous
        self.SCEPower            = DummySound()
        self.waste               = DummySound()
        self.fan                 = pygame.mixer.Sound( 'audio/cabinFan.wav' )
        self.H2OFlow             = DummySound() # continuous
        self.intLights           = DummySound() # continuous
        self.suitComp            = DummySound() # continuous

        # ABORT
        self.abortPad            = DummySound()
        self.abortI              = DummySound()
        self.abortII             = DummySound()
        self.abortII             = DummySound()
        self.abortSIVB           = DummySound()
        self.abortSomething      = DummySound()

        # BOOSTER 
        self.spsThruster         = pygame.mixer.Sound( 'audio/rocket.wav' ) # continuous
        self.teiThruster         = DummySound() # continuous
        self.tliThruster         = DummySound() # continuous
        self.sicThruster         = DummySound() # continuous
        self.siiThruster         = DummySound() # continuous
        self.sivbThruster        = DummySound() # continuous
        self.miThruster          = DummySound() # continuous
        self.miiThruster         = DummySound() # continuous
        self.miiiThruster        = DummySound() # continuous

        # C&WS

        # CAPCOM
        self.quindarin           = pygame.mixer.Sound( 'audio/quindar-in.wav' )
        self.quindarout          = pygame.mixer.Sound( 'audio/quindar-out.wav' )

        # EVENT SEQUENCE
        self.ES1                 = pygame.mixer.Sound( 'audio/ES1.wav' )
        self.ES2                 = pygame.mixer.Sound( 'audio/ES2.wav' )
        self.ES3                 = DummySound()
        self.ES4                 = DummySound()
        self.ES5                 = DummySound()
        self.ES6                 = DummySound()
        self.ES7                 = DummySound()
        self.ES8                 = DummySound()
        self.ES9                 = DummySound()
        self.ES10                = DummySound()

        # CRYOGENICS
        self.o2fan               = pygame.mixer.Sound( 'audio/o2fan.wav' ) # continuous
        self.h2fan               = pygame.mixer.Sound( 'audio/h2fan.wav' ) # continuous
        self.pumps               = DummySound() # continuous
        self.heat                = DummySound() # continuous

        # PYROTECHNICS
        self.csmDeploy           = pygame.mixer.Sound( 'audio/csmDeploy.wav' )

