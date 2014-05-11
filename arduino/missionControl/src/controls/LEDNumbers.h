#ifndef _LEDNUMBERS_H
#define _LEDNUMBERS_H

#include "LEDNumber.h"

extern LED ABR0[8];
extern LED ABR1[8];
extern LED ABR2[8];
extern LED AHR0[8];
extern LED AHR1[8];
extern LED AHR2[8];
extern LED IHR0[8];
extern LED IHR1[8];
extern LED IHR2[8];

class LEDNumbers {
  public:
    LEDNumber* findLEDNumber( char* label );
    void clear( void );
    void test( void );
};

#endif
