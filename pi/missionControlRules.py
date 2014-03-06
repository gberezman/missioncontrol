#!/usr/bin/env python

from boardSignalTransformer import BoardSignalTransformer

class MissionControlRules:

    def applyRules(self, switches):
        transformer = BoardSignalTransformer()
       
        leds = [] 
        if transformer.isSwitchOn( 'SPS', switches ):
            leds.append( 'Thrust Indicator' )

        return transformer.getLedArray( leds )
