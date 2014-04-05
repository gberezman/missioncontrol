#ifndef _LEDDIGITS_H
#define _LEDDIGITS_H

#include "LEDDigit.h"

class LEDDigits {
  public:
    LEDDigit* findLEDDigit( char* label );
    void clear( void );
};

#endif
