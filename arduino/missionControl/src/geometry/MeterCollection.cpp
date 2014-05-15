#include "MeterCollection.h"

extern Adafruit_LEDBackpack matrixA;
extern Adafruit_LEDBackpack matrixB;
extern Adafruit_LEDBackpack matrixC;
extern Adafruit_LEDBackpack matrixD;
extern Adafruit_LEDBackpack matrixE;

LEDMeter MeterCollection::METERS[] = { 
  // CRYOGENICS
  LEDMeter( "H2Pressure", &matrixC, 0, 0, TWELVE_BAR_MIDRANGE_COLORS ),
  LEDMeter( "O2Qty",      &matrixC, 0, 8, TWELVE_BAR_QTY_COLORS ),
  LEDMeter( "O2Pressure", &matrixC, 3, 0, TWELVE_BAR_MIDRANGE_COLORS ),
  LEDMeter( "H2Qty",      &matrixC, 3, 8, TWELVE_BAR_QTY_COLORS ),

  // INCO
  LEDMeter( "Signal1",    &matrixD, 0, 0, ALL_YELLOW ),
  LEDMeter( "Signal2",    &matrixD, 3, 0, ALL_YELLOW )

  // EECOM
  // LEDMeter( "Voltage",    &matrixE, 0, 0, TWELVE_BAR_QTY_COLORS ),
  // LEDMeter( "Current",    &matrixE, 0, 8, TWELVE_BAR_MIDRANGE_COLORS ),
  // LEDMeter( "Resistance", &matrixE, 3, 0, TWELVE_BAR_MIDRANGE_COLORS ),
  // LEDMeter( "O2Flow",     &matrixE, 3, 8, TWELVE_BAR_MIDRANGE_COLORS ),
};

LEDMeter* MeterCollection::getMeter( char* label ) {
  for( int i = 0; i < sizeof( METERS ) / sizeof( LEDMeter ); i++ )
    if( strcmp( label, METERS[i].getLabel() ) == 0 )
        return &METERS[i];

  return NULL;
}

void MeterCollection::testAll( void ) {
  for( int bars = 0; bars < 13; bars++ ) {
    for( int i = 0; i < sizeof( METERS ) / sizeof( LEDMeter ); i++ )
        METERS[i].setBars(bars);
    delay( 20 );
  }
}

void MeterCollection::clearAll( void ) {
  for( int i = 0; i < sizeof( METERS ) / sizeof( LEDMeter ); i++ )
    METERS[i].setBars(0);
}
