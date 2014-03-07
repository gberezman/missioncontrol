#include <Wire.h>
#include "Adafruit_MCP23017.h"

Adafruit_MCP23017 mcp0;


uint8_t buttonStates[64];
  
void setup() {  
  for( int i = 0; i < 64; i++ ) {
    buttonStates[i] = 0;
  }

  mcp0.begin(0);

  mcp0.pinMode(0, INPUT);
  mcp0.pullUp(0, HIGH);  // 100K pullup 
}

void loop() {
  scanSwitches();
}

void scanSwitches() {
  byte current[16];
  uint16t mcp0States = mcp0.readGPIOAB();
  for( int i = 0; i < 16; i++ ) {
    if( mcp0States & (1 << i) ) {
      current[i] = 1;
    } else {
      current[i] = 0;
    }
  }

  for( int i = 0; i < 16; i++ ) {
    if( ( current[i] == 0 ) && ( state[i] == 1 ) ) {
        Serial.write(i + 128);
        state[i] = current[i];
    } else if ( ( current[i] == 1 ) && ( state[i] == 0 ) ) {
        Serial.write(i);
        state[i] = current[i];
    }
  }
}
