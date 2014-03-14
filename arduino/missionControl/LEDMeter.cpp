#include <Wire.h>
#include "LEDMeter.h"

const static uint8_t numbers[][3] = {
    { B00000000, B00000000, B00000000 },
    { B00010001, B00000000, B00000000 },
    { B00110011, B00000000, B00000000 },
    { B01110111, B00000000, B00000000 },
    { B11111111, B00000000, B00000000 },
    { B11111111, B00010001, B00000000 },
    { B11111111, B00110011, B00000000 },
    { B11111111, B01110111, B00000000 },
    { B11111111, B11111111, B00000000 },
    { B11111111, B11111111, B00010001 },
    { B11111111, B11111111, B00110011 },
    { B11111111, B11111111, B01110111 },
    { B11111111, B11111111, B11111111 }
};

LEDMeter::LEDMeter(Adafruit_LEDBackpack* _matrix, uint8_t _baseCathode, uint8_t _baseAnode, uint16_t* _colors) {
    baseCathode = _baseCathode;
    baseAnode   = _baseAnode;
    matrix      = _matrix;
    colors      = _colors;
}

void LEDMeter::clear(void) {
  for( int cathode = baseCathode; cathode < baseCathode + 3; cathode++ ) 
    matrix->displaybuffer[cathode] = 0;
    
  matrix->writeDisplay();
}

void LEDMeter::setBars(uint8_t bars) {  
  for( int pin = baseCathode; pin < baseCathode + 3; pin++ ) 
    setDisplayBuffer( pin, numbers[bars][pin - baseCathode], getColor( bars ) );    
  
  matrix->writeDisplay();
}

void LEDMeter::setDisplayBuffer( uint8_t pin, uint8_t value, uint8_t color ) {
  matrix->displaybuffer[pin] = applyNewAnodes(matrix->displaybuffer[pin], value & color);
}

uint16_t LEDMeter::applyNewAnodes( uint16_t current, uint8_t value ) {
  uint16_t mask = ~ ( B11111111 << baseAnode );
  return ( current & mask ) | ( value << baseAnode );  
}

uint8_t LEDMeter::getColor( uint8_t bars ) {
  if( bars >= 1 )
    return colors[bars - 1];
  else 
    return 0;
}

/*
// O2 press, H2 press, O2 Qty, H2 Qty, Voltage, current, O2flow, Resistance
uint8_t meterBars[] = { 0 }; // bars: 1-12
// { matrix index, cathod offset, anode offset }
uint8_t meterGeometry[][3] = { 
    { 0, 0, 0 },
    { 0, 0, 8 },
    { 0, 3, 0 },
    { 0, 3, 8 },
    { 1, 0, 0 },
    { 1, 0, 8 },
    { 1, 3, 0 },
    { 1, 3, 8 }
};

#define NUM_METERS sizeof(meterBars)/sizeof(uint8_t)

*/

/*
void setMeterValueOrig() { 

  uint8_t geometry[] = meterGeometry[graphIdx];
  Adafruit_LEDBackpack matrix = matrices[geometry[0]];
  uint8_t cathodeOffset = geometry[1];
  uint8_t anodeOffset  = geometry[2];

  uint8_t colorMask = getColorMask( bars );

  for( int cathode = cathodeOffset; cathode < 3 + cathodeOffset; cathode++ ) {
    uint16_t buffer = matrix.displaybuffer[cathode];

    buffer = disableByteAtOffset( buffer, anodeOffset );
    buffer |= (colorMask & numbers[bars - 1][3 - cathode]) << anodeOffset; // enable number

    matrix.displaybuffer[cathode] = buffer;

    matrix.writeDisplay();
  }

}

uint16_t disableByteAtOffset( uint16_t value, uint8_t offset ) {
  uint16_t anodesMask = B11111111 << offset;
  return value & ( ~anodesMask );
}

uint8_t getColorMask( uint8_t bars ) {
  if( bars < 2 )
    return LED_RED;
  else if( bars < 4 )
    return LED_YELLOW;
  else
    return LED_GREEN;
}

*/
