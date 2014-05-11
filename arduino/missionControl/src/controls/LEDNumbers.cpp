#include "LEDNumbers.h"
#include "../geometry/LEDNumberGeometry.h"
#include <Arduino.h>

void LEDNumbers::clear( void ) {
    for( int i = 0; i < sizeof( NUMBERS ) / sizeof( LEDNumber ); i++ )
        NUMBERS[i].clear();
}

LEDNumber* LEDNumbers::findLEDNumber( char* label ) {
  for( int i = 0; i < sizeof( NUMBERS ) / sizeof( LEDNumber ); i++ )
    if( strcmp( label, NUMBERS[i].getLabel() ) == 0 )
        return &NUMBERS[i];

  return NULL;
}

void LEDNumbers::test( void ) {
    char buffer[4];
    for( int value = 0; value < 1000; value += 111 ) {
        itoa( value, buffer, 10 );
        for( int i = 0; i < sizeof( NUMBERS ) / sizeof( LEDNumber ); i++ ) {
            NUMBERS[i].set( buffer );
        }
        delay( 200 );
    }
}
