#include "Potentiometers.h"
#include "../geometry/PotentiometerGeometry.h"

void Potentiometers::scan( void ) {
    for( int i = 0; i < sizeof( POTENTIOMETERS ) / sizeof( Potentiometer ); i++ ) {
        POTENTIOMETERS[i].scan();
        delay(2); // recommended pause when accessing analog pins
    }
}

void Potentiometers::sendPotStates( void ) {
    for( int i = 0; i < sizeof( POTENTIOMETERS ) / sizeof( Potentiometer ); i++ )
        if( POTENTIOMETERS[i].hasChanged() )
            POTENTIOMETERS[i].sendToSerial();
}
