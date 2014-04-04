#ifndef _SWITCH_EXPANDER_H
#define _SWITCH_EXPANDER_H

#include "Arduino.h"
#include "Adafruit_MCP23017.h"

#define NUM_EXPANDER_PINS 16

class SwitchExpander {
  public:
    SwitchExpander(uint8_t _address, char* _pinLabels[]);
    void initialize();
    void scanSwitches(void);
    bool wasPinTurnedOn( uint8_t _pin );
    bool wasPinTurnedOff( uint8_t _pin );
    bool didPinChangeState( uint8_t pin );
    void sendChangedStatesToSerial();
    char* getPinId( uint8_t _pin );

  private:
    void sendStateToSerial( uint8_t pin );
    void invertSwitches( void );
    char** pinLabels;
    uint8_t address;
    Adafruit_MCP23017 mcp;
    uint8_t prevSwitchStates[NUM_EXPANDER_PINS];
    uint8_t currSwitchStates[NUM_EXPANDER_PINS];
    bool initialized;

    void storePreviousSwitchStates(void);
};

#endif
