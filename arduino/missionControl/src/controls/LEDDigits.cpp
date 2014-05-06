#include "LEDDigits.h"
#include "../geometry/LEDDigitGeometry.h"

void LEDDigits::clear( void ) {
    for( int i = 0; i < sizeof( DIGITS ) / sizeof( LEDDigit ); i++ )
        DIGITS[i].clear();
}

LEDDigit* LEDDigits::findLEDDigit( char* label ) {
  for( int i = 0; i < sizeof( DIGITS ) / sizeof( LEDDigit ); i++ )
    if( strcmp( label, DIGITS[i].getLabel() ) == 0 )
        return &DIGITS[i];

  return NULL;
}

