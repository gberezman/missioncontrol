#!/usr/bin/env python

class BoardState:

    def __init__(self, config):

        self.config = config

        self.switchState = {}
        for switch in config.switches:
            self.switchState[switch] = False

        self.potState = {}
        for pot in config.potentiometers:
            self.potState[pot] = 0

        self.ledStates = {}
        for led in config.ledIndicators:
            self.ledStates[led] = False

        self.scaledIndicatorStates = {}
        for indicator in config.scaledIndicators:
            self.scaledIndicatorStates[indicator] = 0

    def enableSwitch(self, switch):
        self.switchState[switch] = True

    def isSwitchEnabled(self, switch):
        return self.switchState[switch]

    def getClearedSwitches(self):
        return bytearray(len(self.switches))

    def setPotentiometer(self, pot, value):
        self.potState[pot] = value

    def getPotentiometer(self, pot):
        return self.potState[pot]

    def isLedEnabled(self, led):
        return self.ledStates[led]

    def enableLed(self, led):
        self.ledStates[led] = True

    def getScaledIndicator(self, indicator):
        return self.scaledIndicatorStates[indicator]

    def setScaledIndicator(self, indicator, value):
        self.scaledIndicatorStates[indicator] = value
