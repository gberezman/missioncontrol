#include "LEDDigits.h"

LEDDigits::LEDDigits( LEDDigit _digits[] ) {
    digits = _digits;
}

void LEDDigits::clear( void ) {
    for( int i = 0; i < sizeof( digits ) / sizeof( LEDDigit ); i++ )
        digits[i].clear();
}

LEDDigit* LEDDigits::findLEDDigit( char* label ) {
  for( int i = 0; i < sizeof( digits ) / sizeof( LEDDigit ); i++ )
    if( strcmp( label, digits[i].getLabel() ) == 0 )
        return &digits[i];
}

