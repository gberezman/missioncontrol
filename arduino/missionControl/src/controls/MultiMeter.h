#ifndef _MULTIMETER_H
#define _MULTIMETER_H

#include <Arduino.h>
#include "LEDMeter.h"

class MultiMeter {
  public:
    MultiMeter( LEDMeter* loMeter, LEDMeter* hiMeter );
    void test( void );
    void clear( void );
    void enableRange( int8_t lo, int8_t hi );

  private:
    LEDMeter* loMeter;
    LEDMeter* hiMeter;
};

#endif
