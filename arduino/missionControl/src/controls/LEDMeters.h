#ifndef _METERS_H
#define _METERS_H

#include "LEDMeter.h"

class LEDMeters {
  public:
    LEDMeter* findLEDMeter( char* label );
};

#endif
