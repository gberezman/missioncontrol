#include "LEDMeters.h"

LEDMeters::LEDMeters( LEDMeter _meters[] ) {
    meters = _meters;
}

LEDMeter* LEDMeters::findLEDMeter( char* meterLabel ) {
  for( int i = 0; i < sizeof( meters ) / sizeof( LEDMeter ); i++ )
    if( strcmp( meterLabel, meters[i].getLabel() ) == 0 )
        return &meters[i];
}

