#ifndef _SWITCH_EXPANDER_H
#define _SWITCH_EXPANDER_H

#include <Wire.h>
#include "Adafruit_MCP23017.h"

#define NUM_EXPANDER_PINS 16

class SwitchExpander {
  public:
    SwitchExpander(uint8_t _address);
    void scanSwitches(void);
    bool isPinTurnedOn( uint8_t _pin );
    bool isPinTurnedOff( uint8_t _pin );
    uint8_t getPinId( uint8_t _pin );

  private:
    void ensureInitialized();
    uint8_t address;
    Adafruit_MCP23017 mcp;
    uint8_t prevSwitchStates[NUM_EXPANDER_PINS];
    uint8_t currSwitchStates[NUM_EXPANDER_PINS];
    bool initialized = false;

    void storePreviousSwitchStates(void);
};

#endif
