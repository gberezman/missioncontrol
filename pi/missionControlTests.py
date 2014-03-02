#!/usr/bin/env python

import unittest
from missionControl import Readings

class MissionControlTests(unittest.TestCase):

    def test_getArmAbortSwitch_returnsZeroZeroCoordinate(self):
        readings = Readings()
        coordinates = readings.switches['Arm Abort']
        self.assertEquals( 0, coordinates[0] )
        self.assertEquals( 0, coordinates[1] )

    def test_getArmAbortSwitchValue_whenOff_returnsOff(self):
        readings = Readings()
        isArmAbortSwitchOn = readings.isSwitchOn('Arm Abort', bytearray([0x0]))
        self.assertFalse( isArmAbortSwitchOn )

    def test_getArmAbortSwitchValue_whenOn_returnsOn(self):
        readings = Readings()
        isArmAbortSwitchOn = readings.isSwitchOn('Arm Abort', bytearray([0x1]))
        self.assertTrue( isArmAbortSwitchOn )

    def test_getArmAbortSwitchValue_whenAbsent_returnsNone(self):
        readings = Readings()
        isArmAbortSwitch = readings.isSwitchOn('Absent Switch', bytearray())
        self.assertIsNone( isArmAbortSwitch )

    def test_getSCEPowerValue_whenOn_returnsOn(self):
        readings = Readings()
        isSCEPowerSwitchOn = readings.isSwitchOn('SCE Power', bytearray([0x0, 0x40]))
        self.assertTrue( isSCEPowerSwitchOn )

    def test_getSCEPowerValue_whenOff_returnsOff(self):
        readings = Readings()
        isSCEPowerSwitchOn = readings.isSwitchOn('SCE Power', bytearray([0x0, 0x30]))
        self.assertFalse( isSCEPowerSwitchOn )

    def test_getSCEPowerValue_whenNotEnoughSegments_returnsNone(self):
        readings = Readings()
        isSCEPowerSwitch = readings.isSwitchOn('SCE Power', bytearray([0x0]))
        self.assertIsNone( isSCEPowerSwitch )

    def test_getAlarmMode_returnsMode(self):
        readings = Readings()
        alarmMode = readings.getPotentiometerReading('Voltage', bytearray([50]))
        self.assertEquals(50, alarmMode)

    def test_getPotReading_forMissingPot_returnsNone(self):
        readings = Readings()
        pot = readings.getPotentiometerReading('Missing Pot', bytearray([50]))
        self.assertIsNone(pot)

    def test_getPotReading_forMissingData_returnsNone(self):
        readings = Readings()
        beam = readings.getPotentiometerReading('Beam', bytearray([50]))
        self.assertIsNone(beam)

    def test_getCurrentReading_returnsCurrentReading(self):
        readings = Readings()
        current = readings.getPotentiometerReading('Current', bytearray([1, 2, 3]))
        self.assertEquals(3, current)

if __name__ == '__main__':
    unittest.main()
