#include "LEDMeters.h"
#include "../geometry/LEDMeterGeometry.h"

LEDMeter* LEDMeters::findLEDMeter( char* meterLabel ) {
  for( int i = 0; i < sizeof( METERS ) / sizeof( LEDMeter ); i++ )
    if( strcmp( meterLabel, METERS[i].getLabel() ) == 0 )
        return &METERS[i];

  return NULL;
}

void LEDMeters::test( void ) {
  for( int bars = 0; bars < 13; bars++ ) {
    for( int i = 0; i < sizeof( METERS ) / sizeof( LEDMeter ); i++ )
        METERS[i].setBars(bars);
    delay( 100 );
  }
}

void LEDMeters::clear( void ) {
  for( int i = 0; i < sizeof( METERS ) / sizeof( LEDMeter ); i++ )
    METERS[i].setBars(0);
}
