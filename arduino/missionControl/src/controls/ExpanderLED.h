#ifndef _EXPANDERLED_H
#define _EXPANDERLED_H

#include <Arduino.h>
#include "Adafruit_MCP23017.h"

class ExpanderLED {

  public:
    ExpanderLED(char* label, Adafruit_MCP23017* mcp, int pin, bool doInvert);
    void initialize( void );
    char* getLabel(void);
    void set( bool turnOn );
    void high(void);
    void low(void);

  private:
    Adafruit_MCP23017* mcp;
    char* label;
    int pin;
    bool doInvert;
    static ExpanderLED expanderLeds[];
};

#endif
