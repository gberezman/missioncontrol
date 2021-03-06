#ifndef _MULTIMETER_H
#define _MULTIMETER_H

#include <Arduino.h>
#include "LEDMeter.h"
#include "LEDNumber.h"

class MultiMeter {
  public:
    void setMeters( LEDMeter* loMeter, LEDMeter* hiMeter );
    void test( void );
    void clear( void );
    void enableRange( int8_t lo, int8_t hi );
    void setColor( int8_t bar, int8_t color );

  private:
    LEDMeter* loMeter;
    LEDMeter* hiMeter;
};

#endif
