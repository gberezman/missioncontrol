#include "LEDs.h"
#include <Arduino.h>
#include "../geometry/LEDGeometry.h"

void LEDs::clear( void ) {
  for( int i = 0; i < sizeof( LEDS ) / sizeof( LED ); i++ )
    LEDS[i].off();
}

void LEDs::test( void ) {
  for( int i = 0; i < sizeof( LEDS ) / sizeof( LED ); i++ )
    LEDS[i].on();
}

LED* LEDs::findLED( char* label ) {
  for( int i = 0; i < sizeof( LEDS ) / sizeof( LED ); i++ )
    if( strcmp( label, LEDS[i].getLabel() ) == 0 )
        return &LEDS[i];
}
