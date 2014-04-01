#include <Wire.h>
#include "LEDMeter.h"

const static uint8_t anodeSegmentForBars[][3] = {
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

LEDMeter::LEDMeter(char* _label, Adafruit_LEDBackpack* _matrix, uint8_t _baseCathode, uint8_t _baseAnode, uint16_t* _colors) {
    baseCathode = _baseCathode;
    baseAnode   = _baseAnode;
    matrix      = _matrix;
    colors      = _colors;
    anodeMask   = ~ ( B11111111 << baseAnode );
    label = _label;
}

char* LEDMeter::getLabel(void) {
    return label;
}

void LEDMeter::clear(void) {
  for( int cathode = baseCathode; cathode < baseCathode + 3; cathode++ ) 
    matrix->displaybuffer[cathode] &= anodeMask;
    
  matrix->writeDisplay();
}

void LEDMeter::setBars(uint8_t bars) {  
  for( int cathodeOffset = 0; cathodeOffset < 3; cathodeOffset++ ) {
    uint8_t anodeSegment = anodeSegmentForBars[bars][cathodeOffset];
    setDisplayBuffer( cathodeOffset + baseCathode, anodeSegment, getColor( bars ) );
  }
  
  matrix->writeDisplay();
}

void LEDMeter::setDisplayBuffer( uint8_t pin, uint8_t value, uint8_t color ) {
  matrix->displaybuffer[pin] = applyNewAnodes(matrix->displaybuffer[pin], value & color);
}

uint16_t LEDMeter::applyNewAnodes( uint16_t current, uint8_t value ) {
  return ( current & anodeMask ) | ( value << baseAnode );  
}

uint8_t LEDMeter::getColor( uint8_t bars ) {
  return bars >= 1 ? colors[bars - 1 ] : 0;
}

