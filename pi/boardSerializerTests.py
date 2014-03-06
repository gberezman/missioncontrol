#!/usr/bin/env python

import unittest
from boardSerializer import BoardSerializer
from boardState import BoardState

class BoardSerializerTests(unittest.TestCase):
    def setUp(self):
        self.config = TestConfig()
        self.serializer = BoardSerializer()
        self.board = BoardState(self.config)

    def test_serializeUnsetLeds(self):
        ledArray = self.serializer.getLeds(self.board)
        for led in ledArray:
            self.assertEquals( 0, led )

    def test_serializeOneSetLed(self):
        self.board.enableLed( 'LED 1' )
        ledArray = self.serializer.getLeds(self.board)
        self.assertEquals( 1, ledArray[0] )

    def test_serializeSecondLed(self):
        self.board.enableLed( 'LED 2' )
        ledArray = self.serializer.getLeds(self.board)
        self.assertEquals( 2, ledArray[0] )

    def test_serializeThirdLed(self):
        self.board.enableLed( 'LED 3' )
        ledArray = self.serializer.getLeds(self.board)
        self.assertEquals( 4, ledArray[0] )

    def test_serializeMultipleLeds(self):
        self.board.enableLed( 'LED 1' )
        self.board.enableLed( 'LED 2' )
        self.board.enableLed( 'LED 3' )
        ledArray = self.serializer.getLeds(self.board)
        self.assertEquals( 7, ledArray[0] )

    def test_serializeLedOnAnotherByte(self):
        self.board.enableLed( 'LED 4' )
        ledArray = self.serializer.getLeds(self.board)
        self.assertEquals( 1, ledArray[1] )

    def test_serializeUnsetScaledIndicators(self):
        indicators = self.serializer.getScaledIndicators(self.board)
        for value in indicators:
            self.assertEquals(0, value)

    def test_serializeOneScaledIndicator(self):
        self.board.setScaledIndicator('SI 1', 10)
        indicators = self.serializer.getScaledIndicators(self.board)
        self.assertEquals(10, indicators[0])

    def test_serializeSecondScaledIndicator(self):
        self.board.setScaledIndicator('SI 2', 20)
        indicators = self.serializer.getScaledIndicators(self.board)
        self.assertEquals(20, indicators[1])

    def test_deserializeSwitch1(self):
        switches = bytearray([1, 0])
        self.serializer.deserializeSwitches(self.board, switches)
        self.assertTrue( self.board.isSwitchEnabled( 'Switch 1' ) )

    def test_deserializeSwitch2(self):
        switches = bytearray([2, 0])
        self.serializer.deserializeSwitches(self.board, switches)
        self.assertTrue( self.board.isSwitchEnabled( 'Switch 2' ) )

    def test_deserializeSwitch3(self):
        switches = bytearray([0, 1])
        self.serializer.deserializeSwitches(self.board, switches)
        self.assertTrue( self.board.isSwitchEnabled( 'Switch 3' ) )

    def test_deserializeMultipleSwitches(self):
        switches = bytearray([3, 1])
        self.serializer.deserializeSwitches(self.board, switches)
        self.assertTrue( self.board.isSwitchEnabled( 'Switch 1' ) )
        self.assertTrue( self.board.isSwitchEnabled( 'Switch 2' ) )
        self.assertTrue( self.board.isSwitchEnabled( 'Switch 3' ) )
   
    def test_deserializeOffSwitch_setsToOff(self):
        self.board.enableSwitch( 'Switch 1' )
        switches = bytearray([0, 0])
        self.serializer.deserializeSwitches(self.board, switches)
        self.assertFalse( self.board.isSwitchEnabled( 'Switch 1' ) )
        

    def test_deserializePot(self):
        pots = bytearray([10, 0])
        self.serializer.deserializePots(self.board, pots)
        self.assertEquals(10, self.board.getPotentiometer('Pot 1') )

    def test_deserializeSecondPot(self):
        pots = bytearray([0, 20])
        self.serializer.deserializePots(self.board, pots)
        self.assertEquals(20, self.board.getPotentiometer('Pot 2') )

class TestConfig:

    def __init__(self):
        self.switches = { 
            'Switch 1' : [0,0],
            'Switch 2' : [0,1],
            'Switch 3' : [1,0]
        }

        self.potentiometers = {
            'Pot 1' : 0,
            'Pot 2' : 1
        }

        self.ledIndicators = {
            'LED 1' : [0,0],
            'LED 2' : [0,1],
            'LED 3' : [0,2],
            'LED 4' : [1,0]
        }

        self.scaledIndicators = {
            'SI 1' : 0,
            'SI 2' : 1
        }

if __name__ == '__main__':
    unittest.main()
