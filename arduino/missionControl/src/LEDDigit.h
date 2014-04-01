#ifndef _LEDDIGIT_H
#define _LEDIGIT_H

#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
#include "Adafruit_MCP23017.h"

class LEDDigit {
  public:
    LEDDigit(char* label, Adafruit_LEDBackpack* matrix, uint8_t cathode, uint8_t baseAnode);
    void clear(void);
    void setDigit(uint8_t value);
    char* getLabel( void );

  private:
    Adafruit_LEDBackpack* matrix;
    char*    label;
    uint8_t  cathode;
    uint8_t  baseAnode;
};

#endif
