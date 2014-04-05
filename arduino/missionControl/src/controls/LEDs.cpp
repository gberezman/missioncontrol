#include "LEDs.h"
#include "../geometry/LEDGeometry.h"

void LEDs::clear( void ) {
  for( int i = 0; i < sizeof( LEDS ) / sizeof( LED ); i++ )
    LEDS[i].off();
}

LED* LEDs::findLED( char* label ) {
  for( int i = 0; i < sizeof( LEDS ) / sizeof( LED ); i++ )
    if( strcmp( label, LEDS[i].getLabel() ) == 0 )
        return &LEDS[i];
}
