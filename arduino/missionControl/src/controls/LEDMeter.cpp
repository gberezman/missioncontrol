#include <Wire.h>
#include "LEDMeter.h"
#include <math.h>

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

LEDMeter::LEDMeter(char* _label, Adafruit_LEDBackpack* _matrix, uint8_t _baseCathode, uint8_t _baseAnode, uint16_t _colors[12]) {
    baseCathode = _baseCathode;
    baseAnode   = _baseAnode;
    matrix      = _matrix;
    anodeMask   = ~ ( B11111111 << baseAnode );
    label = _label;

    for( int i = 0; i < 12; i++ )
        colors[i] = _colors[i];
}

char* LEDMeter::getLabel(void) {
    return label;
}

void LEDMeter::clear(void) {
  stageClear();
  matrix->writeDisplay();
}

void LEDMeter::stageClear(void) {
  for( int cathode = baseCathode; cathode < baseCathode + 3; cathode++ ) 
    matrix->displaybuffer[cathode] &= anodeMask;
}

void LEDMeter::setBars(uint8_t bars) {  
  for( int cathodeOffset = 0; cathodeOffset < 3; cathodeOffset++ ) {
    uint8_t anodeSegment = anodeSegmentForBars[bars][cathodeOffset];
    setDisplayBuffer( cathodeOffset + baseCathode, anodeSegment, getColor( bars ) );
  }
  
  matrix->writeDisplay();
}

void LEDMeter::setDisplayBuffer( uint8_t cathodePin, uint8_t value, uint8_t color ) {
  matrix->displaybuffer[cathodePin] = applyNewAnodes(matrix->displaybuffer[cathodePin], value & color);
}

uint16_t LEDMeter::applyNewAnodes( uint16_t current, uint8_t value ) {
  return ( current & anodeMask ) | ( value << baseAnode );  
}

uint8_t LEDMeter::getColor( uint8_t bars ) {
  return bars >= 1 ? colors[bars - 1] : 0;
}

void LEDMeter::enableBar( uint8_t bar ) {
  if( bar > 0 ) {
      stageEnableBar( bar );
      matrix->writeDisplay();
  }
}

void LEDMeter::stageEnableBar( uint8_t bar ) {
  if( bar > 0 ) {
      uint8_t cathodePin = baseCathode + ceil( bar/4.0f ) - 1;
      uint16_t current = matrix->displaybuffer[cathodePin];

      uint16_t bit = B1 << ( ( bar - 1 ) % 4 );
      uint16_t bits = ( bit << 4 ) | bit;
      uint16_t colored = bits & getColor( bar );
      uint16_t shifted = colored << baseAnode;
      matrix->displaybuffer[cathodePin] = current | shifted;
  }
}


void LEDMeter::writeDisplay( void ) {
    matrix->writeDisplay();
}

void LEDMeter::setColor( uint8_t bar, uint16_t color ) {
    colors[bar - 1] = color;
}
