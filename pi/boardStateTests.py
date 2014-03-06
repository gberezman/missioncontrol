#!/usr/bin/env python

import unittest
from boardState import BoardState

class BoardStateTests(unittest.TestCase):
    def setUp(self):
        self.board = BoardState(TestConfig())

    def test_switchOnArmAbort(self):
        self.board.enableSwitch( 'Arm Abort' )
        self.assertTrue( self.board.isSwitchEnabled( 'Arm Abort' ) )

    def test_ifArmAbortSwitchIsNotEnabled_switchIsOff(self):
        self.assertFalse( self.board.isSwitchEnabled( 'Arm Abort' ) )

    def test_setVoltagePotentiometer(self):
        self.board.setPotentiometer( 'Voltage', 10 )
        self.assertEquals( 10, self.board.getPotentiometer( 'Voltage' ) )

    def test_unsetVoltage_isZero(self):
        self.assertEquals( 0, self.board.getPotentiometer( 'Voltage' ) )

    def test_unsetAbortLed_isOff(self):
        self.assertFalse( self.board.isLedEnabled( 'Abort' ) )

    def test_enableAbortLed(self):
        self.board.enableLed( 'Abort' )
        self.assertTrue( self.board.isLedEnabled( 'Abort' ) )

    def test_unsetPitch_isZero(self):
        self.assertEquals(0, self.board.getScaledIndicator( 'Pitch' ) )

    def test_setPitchIndicator(self):
        self.board.setScaledIndicator( 'Pitch', 10 )
        self.assertEquals(10, self.board.getScaledIndicator( 'Pitch' ) )

class TestConfig:

    def __init__(self):
        self.switches = { 
            'Arm Abort' : None
        }

        self.potentiometers = {
            'Voltage' : None
        }

        self.ledIndicators = {
            'Abort' : None
        }

        self.scaledIndicators = {
            'Pitch' : None
        }

if __name__ == '__main__':
    unittest.main()
