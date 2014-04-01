#ifndef _SWITCH_EXPANDER_H
#define _SWITCH_EXPANDER_H

#include <Wire.h>
#include "Adafruit_MCP23017.h"

#define NUM_EXPANDER_PINS 16

class SwitchExpander {
  public:
    SwitchExpander(uint8_t _address, char* _pinLabels[]);
    void scanSwitches(void);
    bool wasPinTurnedOn( uint8_t _pin );
    bool wasPinTurnedOff( uint8_t _pin );
    char* getPinId( uint8_t _pin );
    void invert( void );

  private:
    void ensureInitialized();
    char** pinLabels;
    uint8_t address;
    Adafruit_MCP23017 mcp;
    uint8_t prevSwitchStates[NUM_EXPANDER_PINS];
    uint8_t currSwitchStates[NUM_EXPANDER_PINS];
    bool initialized = false;

    void storePreviousSwitchStates(void);
};

#endif
