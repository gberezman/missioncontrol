#ifndef _METERS_H
#define _METERS_H

#include "LEDMeter.h"

class LEDMeters {
  public:
    LEDMeters( LEDMeter meters[] );
    LEDMeter* findLEDMeter( char* label );

  private:
    LEDMeter* meters;
};

#endif
