#ifndef _LEDNUMBER_H
#define _LEDNUMBER_H

#include "LEDDigit.h"

class LEDNumber {
  public:
    LEDNumber( char* label, LEDDigit digits[] );
    void set( char* value );
    void clear( void );
    char* getLabel( void );

  private:
    char* label;
    LEDDigit* digits;

    int getDigit( char* value, int index );
    int charToDigit( char digitChar );
};

#endif
