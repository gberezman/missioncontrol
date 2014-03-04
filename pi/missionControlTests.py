#!/usr/bin/env python

import unittest
from missionControl import Board

class MissionControlTests(unittest.TestCase):

    def test_getArmAbortSwitch_returnsZeroZeroCoordinate(self):
        boards = Board()
        coordinates = boards.switches['Arm Abort']
        self.assertEquals( 0, coordinates[0] )
        self.assertEquals( 0, coordinates[1] )

    def test_getArmAbortSwitchValue_whenOff_returnsOff(self):
        boards = Board()
        isArmAbortSwitchOn = boards.isSwitchOn('Arm Abort', bytearray([0x0]))
        self.assertFalse( isArmAbortSwitchOn )

    def test_getArmAbortSwitchValue_whenOn_returnsOn(self):
        boards = Board()
        isArmAbortSwitchOn = boards.isSwitchOn('Arm Abort', bytearray([0x1]))
        self.assertTrue( isArmAbortSwitchOn )

    def test_getArmAbortSwitchValue_whenAbsent_returnsNone(self):
        boards = Board()
        isArmAbortSwitch = boards.isSwitchOn('Absent Switch', bytearray())
        self.assertIsNone( isArmAbortSwitch )

    def test_getSCEPowerValue_whenOn_returnsOn(self):
        boards = Board()
        isSCEPowerSwitchOn = boards.isSwitchOn('SCE Power', bytearray([0x0, 0x40]))
        self.assertTrue( isSCEPowerSwitchOn )

    def test_getSCEPowerValue_whenOff_returnsOff(self):
        boards = Board()
        isSCEPowerSwitchOn = boards.isSwitchOn('SCE Power', bytearray([0x0, 0x30]))
        self.assertFalse( isSCEPowerSwitchOn )

    def test_getSCEPowerValue_whenNotEnoughSegments_returnsNone(self):
        boards = Board()
        isSCEPowerSwitch = boards.isSwitchOn('SCE Power', bytearray([0x0]))
        self.assertIsNone( isSCEPowerSwitch )

    def test_getAlarmMode_returnsMode(self):
        boards = Board()
        alarmMode = boards.getPotentiometerReading('Voltage', bytearray([50]))
        self.assertEquals(50, alarmMode)

    def test_getPotReading_forMissingPot_returnsNone(self):
        boards = Board()
        pot = boards.getPotentiometerReading('Missing Pot', bytearray([50]))
        self.assertIsNone(pot)

    def test_getPotReading_forMissingData_returnsNone(self):
        boards = Board()
        beam = boards.getPotentiometerReading('Beam', bytearray([50]))
        self.assertIsNone(beam)

    def test_getCurrentReading_returnsCurrentReading(self):
        boards = Board()
        current = boards.getPotentiometerReading('Current', bytearray([1, 2, 3]))
        self.assertEquals(3, current)

    def test_createLedIndicatorsArray_withLampIndicatorOn_setsBit(self):
        indicators = [ 'Lamp Indicator' ];
        boards = Board()
        ledArray = boards.getLedArray( indicators )
        self.assertEquals( 128, ledArray[6] )

    def test_createLedIndicatorsArray_withAckIndicatorOn_setsBit(self):
        indicators = [ 'Ack Indicator' ];
        boards = Board()
        ledArray = boards.getLedArray( indicators )
        self.assertEquals( 1, ledArray[7] )

    def test_createLedIndicatorsArray_withAckIndicatorOn_setsBit(self):
        indicators = [ 'Push To Talk Indicator' ];
        boards = Board()
        ledArray = boards.getLedArray( indicators )
        self.assertEquals( 2, ledArray[0] )
   
    def test_createLedIndicatorsArray_withInvalidIndicator_setsNone(self):
        indicators = [ 'bob' ]
        boards = Board()
        ledArray = boards.getLedArray( indicators )
        self.assertEquals( bytearray([ 0, 0, 0, 0, 0, 0, 0, 0]), ledArray )

if __name__ == '__main__':
    unittest.main()
