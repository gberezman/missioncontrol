#ifndef _LEDS_H
#define _LEDS_H

#include "LED.h"

class LEDs {
  public:
    LEDs( LED leds[] );
    void clear( void );
    LED* findLED( char* label );

  private:
    LED* leds;
};

#endif
