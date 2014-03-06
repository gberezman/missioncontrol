#!/usr/bin/env python

import unittest
from missionControlRules import MissionControlRules
from boardSignalTransformer import BoardSignalTransformer

class MissionControlRulesTests(unittest.TestCase):

    def test_SPSSwitch_turnsOnThrustIndicator(self):
        transformer = BoardSignalTransformer()
        switches = transformer.getClearedSwitches()
        transformer.switchOn( 'SPS', switches )

        rules = MissionControlRules()
        leds = rules.applyRules( switches )

        self.assertTrue( transformer.isLedOn('Thrust Indicator', leds) )

if __name__ == '__main__':
    unittest.main()
