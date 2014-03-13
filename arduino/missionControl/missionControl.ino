#include <Wire.h>
#include "./Adafruit_MCP23017.h"
#include "./Adafruit_LEDBackpack.h"

Adafruit_MCP23017 mcp0;
Adafruit_MCP23017 mcp1;
Adafruit_MCP23017 mcp2;
Adafruit_MCP23017 mcp3;
Adafruit_MCP23017 mcps[] = { mcp0 };

Adafruit_LEDBackpack matrixA;
Adafruit_LEDBackpack matrixB;
Adafruit_LEDBackpack matrixC;
Adafruit_LEDBackpack matrixD;
Adafruit_LEDBackpack matrixE;
Adafruit_LEDBackpack matrices[] = { matrixA };

#define NUM_EXPANDER_PINS 16
#define NUM_EXPANDERS sizeof(mcps)/sizeof(Adafruit_MCP23017)
#define NUM_SWITCHES ( NUM_EXPANDER_PINS ) * ( NUM_EXPANDERS )
#define NUM_MATRICES sizeof(matrices)/sizeof(Adafruit_LEDBackpack)

uint8_t switchStates[NUM_SWITCHES];
  
void setup() {
  Serial.begin(115200);

  initializeBuffers();

  for( int mcp = 0; mcp < NUM_EXPANDERS; mcp++ )
    initializeExpander(mcps[mcp], mcp);

  for( int matrix = 0; matrix < NUM_MATRICES; matrix++ )
    initializeMatrix(matrices[matrix], matrixAddresses[matrix]);
}

void loop() {
  scanSwitches();
  updateMeters();
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

void intializeMatrix(Adafruit_LEDBackpack matrix, int address) {
  matrix.begin(address + 0x70);
  matrix.setBrightness(10);
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

// O2 press, H2 press, O2 Qty, H2 Qty, Voltage, current, O2flow, Resistance
uint8_t meterBars[] = { 0 } // bars: 1-12
// { matrix index, cathod offset, anode offset }
uint8_t meterGeometry[][3] = { 
    { 0, 0, 0 }
    { 0, 0, 8 }
    { 0, 3, 0 }
    { 0, 3, 8 }
    { 1, 0, 0 }
    { 1, 0, 8 }
    { 1, 3, 0 }
    { 1, 3, 8 }
}

#define NUM_METERS sizeof(meterBars)/sizeof(uint8_t)
#define LED_GREEN  B11110000
#define LED_RED    B00001111
#define LED_YELLOW B11111111

void updateMeters() {
  for( int meter = 0; meter < NUM_METERS; meter++ )
    setMeterLED(meterBars[meter], meterGeometry[meter]);
}

uint8_t numbers[][] = {
    { B00000000, B00000000, B00010001 },
    { B00000000, B00000000, B00110011 },
    { B00000000, B00000000, B01110111 },
    { B00000000, B00000000, B11111111 },
    { B00000000, B00010001, B11111111 },
    { B00000000, B00110011, B11111111 },
    { B00000000, B01110111, B11111111 },
    { B00000000, B11111111, B11111111 },
    { B00000000, B11111111, B11111111 },
    { B00010001, B11111111, B11111111 },
    { B00110011, B11111111, B11111111 },
    { B01110111, B11111111, B11111111 },
    { B11111111, B11111111, B11111111 },
}

void setMeterLED(uint8_t bars, uint8_t geometry[]) {
  Adafruit_LEDBackpack matrix = matrices[geometry[0]];
  uint8_t cathodOffset = geometry[1];
  uint8_t anodeOffset  = geometry[2];

  uint8_t colorMask = getColorMask( bars );

  for( int cathode = cathodeOffset; cathode < 3 + cathodeOffset; cathode++ ) {
    uint16_t buffer = matrix.displaybuffer[cathode];

    buffer = disableByteAtOffset( buffer, anodeOffset );
    buffer |= (colorMask & numbers[bars - 1, cathode]) << anodeOffset // enable number

    matrix.displaybuffer[cathode] = buffer;
  }

  matrix.writeDisplay();
}

void disableByteAtOffset( uint16_t value, uint8_t offset ) {
  uint16_t anodesMask = ~ ( B11111111 << anodeOffset );
  return value & anodesMask;
}

uint8_t getColorMask( uint8_t bars ) {
  if( bars < 2 )
    return RED;
  elsif( bars < 4 )
    return YELLOW;
  else
    return GREEN;
}
