#include <Wire.h>
#include "Adafruit_MCP23017.h"
#include "SwitchExpander.h"
#include "Arduino.h"

SwitchExpander::SwitchExpander(uint8_t _address, char* _pinLabels[]) {
  address = _address;
  pinLabels = _pinLabels;
  initialized = false;
}

void SwitchExpander::initialize() {
  if( ! initialized ) {
    mcp.begin(address);
  
    for( int pin = 0; pin < NUM_EXPANDER_PINS; pin++ ) { 
        mcp.pinMode(pin, INPUT);
        mcp.pullUp(pin, HIGH);  // 100K pullup 
    }

    scanSwitches();
    invertSwitches();

    initialized = true;
  }
}

void SwitchExpander::scanSwitches() {
  storePreviousSwitchStates();

  uint16_t gpioState = mcp.readGPIOAB();
  for( uint8_t pin = 0; pin < NUM_EXPANDER_PINS; pin++ )
    currSwitchStates[pin] = ( gpioState & (1 << pin) ) >> pin;
}

void SwitchExpander::invertSwitches() {
  storePreviousSwitchStates();
  for( uint8_t pin = 0; pin < NUM_EXPANDER_PINS; pin++ )
    currSwitchStates[pin] = ! currSwitchStates[pin];
}

bool SwitchExpander::wasPinTurnedOn( uint8_t pin ) {
  return ( prevSwitchStates[pin] == 1 ) && ( currSwitchStates[pin] == 0 );
}

bool SwitchExpander::wasPinTurnedOff( uint8_t pin ) {
  return ( prevSwitchStates[pin] == 0 ) && ( currSwitchStates[pin] == 1 );
}

bool SwitchExpander::didPinChangeState( uint8_t pin ) {
  return wasPinTurnedOn( pin) || wasPinTurnedOff( pin );
}

char* SwitchExpander::getPinId( uint8_t pin ) {
  return pinLabels[pin];
}

void SwitchExpander::storePreviousSwitchStates( void ) {
  for( uint8_t pin = 0; pin < NUM_EXPANDER_PINS; pin++ ) 
    prevSwitchStates[pin] = currSwitchStates[pin];
}

void SwitchExpander::sendChangedStatesToSerial( void ) {
  for( int pin = 0; pin < NUM_EXPANDER_PINS; pin++ ) 
    if( didPinChangeState( pin ) )
       sendStateToSerial( pin );
}

void SwitchExpander::sendStateToSerial( uint8_t pin ) {
  Serial.print( "S " );
  Serial.print( getPinId(pin) );

  if( wasPinTurnedOn( pin ) )
    Serial.print( " 1\n" );
  else if ( wasPinTurnedOff( pin ) )
    Serial.print( " 0\n" );
}
