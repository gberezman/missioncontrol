def bitNumToMask(bitNum):
    offset = bitNum & 31
    return 1 << offset

def isBitSet(bitNum, value):
    mask = bitNumToMask(bitNum)
    return ( value & mask ) != 0

class BoardSerializer:

    def getLeds(self, board):
        leds = bytearray()

        for led in board.config.ledIndicators:
            (segment, bitNum) = board.config.ledIndicators[led]
            self.ensureZerodSegment(leds, segment)
            if( board.isLedEnabled( led ) ):
                self.setLedOn(leds, segment, bitNum)

        return leds

    def getScaledIndicators(self, board):
        indicators = bytearray(len(board.config.scaledIndicators))
        for indicator in board.config.scaledIndicators:
            index = board.config.scaledIndicators[indicator]
            indicators[index] = board.getScaledIndicator(indicator)
        return indicators

    def deserializeSwitches(self, board, switches):
        for switch in board.config.switches:
            (segment, bitNum) = board.config.switches[switch]
            if( isBitSet( bitNum, switches[segment] ) ):
                board.enableSwitch( switch )
            else:
                board.disableSwitch( switch )

    def deserializePots(self, board, pots):
        for pot in board.config.potentiometers:
            value = pots[board.config.potentiometers[pot]]
            board.setPotentiometer(pot, value)

    def ensureZerodSegment(self, ar, size):
        while( len(ar) <= size ):
            ar.append(0)

    def setLedOn(self, leds, segment, bitNum):
        leds[segment] |= bitNumToMask(bitNum)
