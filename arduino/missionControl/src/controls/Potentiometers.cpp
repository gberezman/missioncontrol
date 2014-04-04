#include "Potentiometers.h"

Potentiometers::Potentiometers( Potentiometer _pots[] ) {
    pots = _pots;
}

void Potentiometers::scan( void ) {
    for( int i = 0; i < sizeof( pots ) / sizeof( Potentiometer ); i++ ) {
        pots[i].scan();
        delay(2); // recommended pause when accessing analog pins
    }
}

void Potentiometers::sendPotStates( void ) {
    for( int i = 0; i < sizeof( pots ) / sizeof( Potentiometer ); i++ )
        if( pots[i].hasChanged() )
            pots[i].sendToSerial();
}
