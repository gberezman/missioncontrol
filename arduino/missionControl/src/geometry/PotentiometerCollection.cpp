#include "PotentiometerCollection.h"

Potentiometer PotentiometerCollection::pots[] = { 
  // CAPCOM
  Potentiometer( "Speaker",     A5, 100 ),
  Potentiometer( "Headset",     A6, 100 ),

  // ABORT
  Potentiometer( "AbortMode",   A7, 6 ),

  // EECOM
  Potentiometer( "Resistance",  A8, 12 ),
  Potentiometer( "O2Flow",      A9, 12 ),
  Potentiometer( "Voltage",    A10, 12 ),
  Potentiometer( "Current",    A11, 12 ),

  // INCO
  Potentiometer( "AntPitch",   A12, 12 ),
  Potentiometer( "AntYaw",     A13, 24 ),
  Potentiometer( "Beam",       A14, 12 ),
  Potentiometer( "Tune",       A15, 24 )
};

void PotentiometerCollection::scan( void ) {
    for( int i = 0; i < sizeof( pots ) / sizeof( Potentiometer ); i++ ) {
        pots[i].scan();
        delay(2); // recommended pause when accessing analog pins
    }
};

void PotentiometerCollection::sendPotStates( void ) {
    for( int i = 0; i < sizeof( pots ) / sizeof( Potentiometer ); i++ )
        if( pots[i].hasChanged() )
            pots[i].sendToSerial();
};

Potentiometer* PotentiometerCollection::getPot( char* label ) {
    for( int i = 0; i < sizeof( pots ) / sizeof( Potentiometer ); i++ )
        if( strcmp( label, pots[i].id() ) == 0 ) 
            return &pots[i];

    return NULL;
}
