#ifndef _LEDDIGITS_H
#define _LEDDIGITS_H

#include "LEDDigit.h"

class LEDDigits {
  public:
    LEDDigits( LEDDigit digits[] );
    LEDDigit* findLEDDigit( char* label );
    void clear( void );

  private:
    LEDDigit* digits;
};

#endif
