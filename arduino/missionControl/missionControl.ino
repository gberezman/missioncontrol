#include <Wire.h>
#include "Adafruit_MCP23017.h"

Adafruit_MCP23017 mcp0;

uint8_t state[64];
  
void setup() {  
  Serial.begin(115200);
 
  for( int i = 0; i < 64; i++ ) {
    state[i] = 0;
  }

  mcp0.begin(0);

  for( int pin = 0; pin < 16; pin++ ) { 
    mcp0.pinMode(pin, INPUT);
    mcp0.pullUp(pin, HIGH);  // 100K pullup 
  }
}

void loop() {
  scanSwitches();
}

void scanSwitches() {
  byte current[16];
  uint16_t mcp0States = mcp0.readGPIOAB();
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
