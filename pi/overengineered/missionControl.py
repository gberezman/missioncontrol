#thrusters = ['SPS','TEI','TLI','S-IC','SEI','S-IVB', 'M-I','M-II','M-III']

# Main
#if( anySwitchOf( board, self.thrusters ) ):
    #board.enableLed( 'Thrust' )
    #self.audio.play( self.rocket )
    #sleep(2)
#
    #def anySwitchOf(self, board, switches):
        #for switch in switches:
            #if( board.isSwitchEnabled( switch ) ):
                #return True
        #return False

from audio import Audio
from port import Port
from boardState import BoardState
from boardConfig import BoardConfig
from boardSerializer import BoardSerializer

audio = Audio()
port = Port('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_741333534373512161B1-if00')
board = BoardState(BoardConfig())
serializer = BoardSerializer()

while True:
    pass
