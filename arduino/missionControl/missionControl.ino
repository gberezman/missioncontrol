#include <Wire.h>
#include "./Adafruit_MCP23017.h"

Adafruit_MCP23017 mcp0;
Adafruit_MCP23017 mcp1;
Adafruit_MCP23017 mcp2;
Adafruit_MCP23017 mcp3;
Adafruit_MCP23017 mcps[] = { mcp0 };
// Adafruit_MCP23017 mcps[] = { mcp0, mcp1, mcp2, mcp3 };

#define NUM_EXPANDER_PINS 16
#define NUM_EXPANDERS sizeof(mcps)/sizeof(Adafruit_MCP23017)
#define NUM_SWITCHES ( NUM_EXPANDER_PINS ) * ( NUM_EXPANDERS )

uint8_t switchStates[NUM_SWITCHES];
  
void setup() {
  Serial.begin(115200);
  initializeBuffers();
  for( int mcp = 0; mcp < NUM_EXPANDERS; mcp++ )
    initializeExpander(mcps[mcp], mcp);
}

void loop() {
  scanSwitches();
}

void initializeBuffers() {
  for( int i = 0; i < NUM_SWITCHES; i++ ) 
    switchStates[i] = 0;
}

void initializeExpander(Adafruit_MCP23017 mcp, int address) {
  mcp.begin(address);

  for( int pin = 0; pin < NUM_EXPANDER_PINS; pin++ ) { 
    mcp.pinMode(pin, INPUT);
    mcp.pullUp(pin, HIGH);  // 100K pullup 
  }
}

void scanSwitches() {
  uint8_t current[NUM_SWITCHES];
  
  for( int mcp = 0; mcp < NUM_EXPANDERS; mcp++ )
    scanMCPSwitches(mcps[mcp], current, 16 * mcp);
  
  sendAndUpdateSwitchStateChanges(current);
}

void scanMCPSwitches(Adafruit_MCP23017 mcp, uint8_t states[], int offset) {
  uint16_t gpioState = mcp.readGPIOAB();
  for( int i = 0; i < NUM_EXPANDER_PINS; i++ )
    states[i + offset] = ( gpioState & (1 << i) ) >> i;
}

void sendAndUpdateSwitchStateChanges(uint8_t current[]) {
  for( int i = 0; i < NUM_SWITCHES; i++ ) {
    boolean onToOff = ( switchStates[i] == 1 ) && ( current[i] == 0 );
    boolean offToOn = ( switchStates[i] == 0 ) && ( current[i] == 1 );
    if( onToOff ) {
        Serial.write(i + 128);
        switchStates[i] = current[i];
    } else if ( offToOn ) {
        Serial.write(i);
        switchStates[i] = current[i];
    }
  }
}

