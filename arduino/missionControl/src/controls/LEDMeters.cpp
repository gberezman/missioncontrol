#include "LEDMeters.h"
#include "../geometry/LEDMeterGeometry.h"

LEDMeter* LEDMeters::findLEDMeter( char* meterLabel ) {
  for( int i = 0; i < sizeof( METERS ) / sizeof( LEDMeter ); i++ )
    if( strcmp( meterLabel, METERS[i].getLabel() ) == 0 )
        return &METERS[i];
}
