#ifndef _SWITCH_EXPANDER_CPP
#define _SWITCH_EXPANDER_CPP

#include <Wire.h>
#include "Adafruit_MCP23017.h"
#include "SwitchExpander.h"
#include "Arduino.h"

void SwitchExpander::initialize(uint8_t _address, uint16_t _activePins) {
  address = _address;
  activePins = _activePins;
  
  mcp.begin(address);
  
  for( int pin = 0; pin < NUM_EXPANDER_PINS; pin++ ) { 
      mcp.pinMode(pin, INPUT);
      mcp.pullUp(pin, HIGH);  // 100K pullup 
  }
}

void SwitchExpander::scanSwitches() {
  storePreviousSwitchStates();

  uint16_t gpioState = mcp.readGPIOAB();
  for( uint8_t pin = 0; pin < NUM_EXPANDER_PINS; pin++ )
    if( bitRead( activePins, pin ) )
      currSwitchStates[pin] = ( gpioState & (1 << pin) ) >> pin;
}

bool SwitchExpander::isPinTurnedOn( uint8_t pin ) {
  return ( prevSwitchStates[pin] == 0 ) && ( currSwitchStates[pin] == 1 );
}

bool SwitchExpander::isPinTurnedOff( uint8_t pin ) {
  return ( prevSwitchStates[pin] == 1 ) && ( currSwitchStates[pin] == 0 );
}

uint8_t SwitchExpander::getPinId( uint8_t pin ) {
  return address * 16 + pin;
}

void SwitchExpander::storePreviousSwitchStates(void) {
  for( uint8_t pin = 0; pin < NUM_EXPANDER_PINS; pin++ ) 
    prevSwitchStates[pin] = currSwitchStates[pin];
}

#endif
