#include <Wire.h>
#include "Adafruit_MCP23017.h"
#include "Adafruit_LEDBackpack.h"
#include "LEDMeter.h"

Adafruit_MCP23017 mcp0;
// Adafruit_MCP23017 mcp1;
// Adafruit_MCP23017 mcp2;
// Adafruit_MCP23017 mcp3;
Adafruit_MCP23017 mcps[] = { mcp0 };

Adafruit_LEDBackpack matrixA = Adafruit_LEDBackpack();
// Adafruit_LEDBackpack matrixB;
// Adafruit_LEDBackpack matrixC;
// Adafruit_LEDBackpack matrixD;
// Adafruit_LEDBackpack matrixE;

#define NUM_EXPANDER_PINS 16
#define NUM_EXPANDERS sizeof(mcps)/sizeof(Adafruit_MCP23017)
#define NUM_SWITCHES ( NUM_EXPANDER_PINS ) * ( NUM_EXPANDERS )

uint8_t switchStates[NUM_SWITCHES];
uint8_t potStates[1];
  
uint16_t dialColors[] = { 
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_YELLOW,
  BAR_LED_RED
};

uint16_t meterColors[] = { 
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN
};

LEDMeter o2meter = LEDMeter(&matrixA, 0, 0, dialColors);

void setup() {
  Serial.begin(115200);
  
  Wire.begin();

  initializeSwitchBuffers();

  initializeExpander( mcp0, 0 );
  // initializeExpander( mcp1, 1 );
  // initializeExpander( mcp2, 2 );
  // initializeExpander( mcp3, 3 );

  initializeLEDMatrix( matrixA, 0x70 );
  // initializeLEDMatrix( matrixB, 0x71 );
  // initializeLEDMatrix( matrixC, 0x72 );
  // initializeLEDMatrix( matrixD, 0x73 );
  // initializeLEDMatrix( matrixE, 0x74 );
}

void loop() {
  scanSwitches();
  
  potStates[0] = map( analogRead(7), 0, 1023, 0, 12 );  
  
  updateMeters();
}

void initializeSwitchBuffers() {
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

void initializeLEDMatrix(Adafruit_LEDBackpack matrix, uint8_t address) {
  matrixA.begin( address );
  matrix.clear();  
  matrix.writeDisplay();
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

void updateMeters() {
  o2meter.setBars(potStates[0]);
}

