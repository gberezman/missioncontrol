#include "LEDs.h"

LEDs::LEDs( LED _leds[] ) {
    leds = _leds;
}

void LEDs::clear( void ) {
  for( int i = 0; i < sizeof( leds ) / sizeof( LED ); i++ )
    leds[i].off();
}

LED* LEDs::findLED( char* label ) {
  for( int i = 0; i < sizeof( leds ) / sizeof( LED ); i++ )
    if( strcmp( label, leds[i].getLabel() ) == 0 )
        return &leds[i];
}
