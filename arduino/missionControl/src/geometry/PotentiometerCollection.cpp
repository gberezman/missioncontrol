#include "PotentiometerCollection.h"

Potentiometer PotentiometerCollection::pots[] = { 
  // CAPCOM
  // Potentiometer( "Speaker",    A0 ),
  // Potentiometer( "Headset",    A1 ),

  // ABORT
  // Potentiometer( "AbortMode",  A2 ),

  // EECOM
  // Potentiometer( "Voltage",    A3 ),
  // Potentiometer( "Current",    A4 ),
  // Potentiometer( "Resistance", A5 ),
  // Potentiometer( "O2Flow",     A6 ),

  // INCO
  Potentiometer( "AntPitch",   A12 ),
  Potentiometer( "AntYaw",     A13 ),
  Potentiometer( "Beam",       A14 ),
  Potentiometer( "Tune",       A15 )
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
