#ifndef _LEDDIGIT_H
#define _LEDDIGIT_H

#include "LED.h"

class LEDDigit {
  public:
    LEDDigit(char* label, LED _ledArray[8]);
    void clear(void);
    void setDigit(uint8_t value);
    char* getLabel( void );

  private:
    char* label;
    LED*  ledArray;

    bool numbers[10][8] = {
        { true, true, true, true, true, true, false, false },
        { true, true, false, false, false, false, false, false },
        { true, false, true, true, false, true, true, false },
        { true, true, true, false, false, true, true, false },
        { true, true, false, false, true, false, true, false },
        { false, true, true, false, true, true, true, false },
        { false, true, true, true, true, true, true, false },
        { true, true, false, false, false, true, false, false },
        { true, true, true, true, true, true, true, false },
        { true, true, true, false, true, true, true, false }
    };
};

#endif
