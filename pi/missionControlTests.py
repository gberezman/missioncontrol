#!/usr/bin/env python

import unittest
from missionControl import Board

class MissionControlTests(unittest.TestCase):

    def test_getArmAbortSwitch_returnsZeroZeroCoordinate(self):
        board = Board()
        coordinates = board.switches['Arm Abort']
        self.assertEquals( 0, coordinates[0] )
        self.assertEquals( 0, coordinates[1] )

    def test_getArmAbortSwitchValue_whenOff_returnsOff(self):
        board = Board()
        isArmAbortSwitchOn = board.isSwitchOn('Arm Abort', bytearray([0x0]))
        self.assertFalse( isArmAbortSwitchOn )

    def test_getArmAbortSwitchValue_whenOn_returnsOn(self):
        board = Board()
        isArmAbortSwitchOn = board.isSwitchOn('Arm Abort', bytearray([0x1]))
        self.assertTrue( isArmAbortSwitchOn )

    def test_getArmAbortSwitchValue_whenAbsent_returnsNone(self):
        board = Board()
        isArmAbortSwitch = board.isSwitchOn('Absent Switch', bytearray())
        self.assertIsNone( isArmAbortSwitch )

    def test_getSCEPowerValue_whenOn_returnsOn(self):
        board = Board()
        isSCEPowerSwitchOn = board.isSwitchOn('SCE Power', bytearray([0x0, 0x40]))
        self.assertTrue( isSCEPowerSwitchOn )

    def test_getSCEPowerValue_whenOff_returnsOff(self):
        board = Board()
        isSCEPowerSwitchOn = board.isSwitchOn('SCE Power', bytearray([0x0, 0x30]))
        self.assertFalse( isSCEPowerSwitchOn )

    def test_getSCEPowerValue_whenNotEnoughSegments_returnsNone(self):
        board = Board()
        isSCEPowerSwitch = board.isSwitchOn('SCE Power', bytearray([0x0]))
        self.assertIsNone( isSCEPowerSwitch )

    def test_getAlarmMode_returnsMode(self):
        board = Board()
        alarmMode = board.getPotentiometerReading('Voltage', bytearray([50]))
        self.assertEquals(50, alarmMode)

    def test_getPotReading_forMissingPot_returnsNone(self):
        board = Board()
        pot = board.getPotentiometerReading('Missing Pot', bytearray([50]))
        self.assertIsNone(pot)

    def test_getPotReading_forMissingData_returnsNone(self):
        board = Board()
        beam = board.getPotentiometerReading('Beam', bytearray([50]))
        self.assertIsNone(beam)

    def test_getCurrentReading_returnsCurrentReading(self):
        board = Board()
        current = board.getPotentiometerReading('Current', bytearray([1, 2, 3]))
        self.assertEquals(3, current)

    def test_createLedIndicatorsArray_withLampIndicatorOn_setsBit(self):
        indicators = [ 'Lamp Indicator' ];
        board = Board()
        ledArray = board.getLedArray( indicators )
        self.assertEquals( 128, ledArray[6] )

    def test_createLedIndicatorsArray_withAckIndicatorOn_setsBit(self):
        indicators = [ 'Ack Indicator' ];
        board = Board()
        ledArray = board.getLedArray( indicators )
        self.assertEquals( 1, ledArray[7] )

    def test_createLedIndicatorsArray_withAckIndicatorOn_setsBit(self):
        indicators = [ 'Push To Talk Indicator' ];
        board = Board()
        ledArray = board.getLedArray( indicators )
        self.assertEquals( 2, ledArray[0] )
   
    def test_createLedIndicatorsArray_withInvalidIndicator_setsNone(self):
        indicators = [ 'bob' ]
        board = Board()
        ledArray = board.getLedArray( indicators )
        self.assertEquals( bytearray([ 0, 0, 0, 0, 0, 0, 0, 0]), ledArray )

    def test_createScaledIndicatorsArray_withAHRIndictor_setsValue(self):
        indicators = { 'AHR Indicator': 25 }
        board = Board()
        indicatorArray = board.getScaledIndicatorArray( indicators )
        self.assertEquals( indicatorArray[5], 25 )

    def test_createScaledIndicatorsArray_withInvalidIndicator_ignores(self):
        indicators = { 'bob': 25 }
        board = Board()
        indicatorArray = board.getScaledIndicatorArray( indicators )
        self.assertEquals( bytearray(len(board.scaledIndicators)), indicatorArray)
        
if __name__ == '__main__':
    unittest.main()
