#ifndef _LEDS_H
#define _LEDS_H

#include "LED.h"

class LEDs {
  public:
    void clear( void );
    LED* findLED( char* label );
};

#endif