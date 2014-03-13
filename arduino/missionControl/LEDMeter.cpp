#include <Wire.h>
#include "LEDMeter.h"

LEDMeter::LEDMeter(Adafruit_LEDBackpack* _matrix, uint8_t _baseCathode, uint8_t _baseAnode, uint16_t* _colors) {
    baseCathode = _baseCathode;
    baseAnode   = _baseAnode;
    matrix      = _matrix;
    colors      = _colors;
}

void LEDMeter::clear(void) {
  for( int cathode = baseCathode; cathode < baseCathode + 3; cathode++ ) {
    matrix->displaybuffer[cathode] = 0;
  }
  matrix->writeDisplay();
}

void LEDMeter::setBars(uint8_t bars) {
  // for( int cathode = baseCathode; cathode < baseCathode + 3; cathode++ )
    // matrix->displaybuffer[cathode] = 0;
    
  uint16_t color = 0;
  if( bars >= 1 )
    color = colors[bars - 1];
  
  switch( bars ) {
    case 0:
      matrix->displaybuffer[baseCathode] = 0;
      matrix->displaybuffer[baseCathode + 1] = 0;
      matrix->displaybuffer[baseCathode + 2] = 0;
    case 1:
      matrix->displaybuffer[baseCathode] = B00010001 & color;
      matrix->displaybuffer[baseCathode + 1] = 0;
      matrix->displaybuffer[baseCathode + 2] = 0;
      break;      
    case 2:
      matrix->displaybuffer[baseCathode] = B00110011 & color;
      matrix->displaybuffer[baseCathode + 1] = 0;
      matrix->displaybuffer[baseCathode + 2] = 0;
      break;
    case 3:
      matrix->displaybuffer[baseCathode] = B01110111 & color;
      matrix->displaybuffer[baseCathode + 1] = 0;
      matrix->displaybuffer[baseCathode + 2] = 0;
      break;
    case 4:
      matrix->displaybuffer[baseCathode] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 1] = 0;
      matrix->displaybuffer[baseCathode + 2] = 0;
      break;
    case 5:
      matrix->displaybuffer[baseCathode] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 1] = B00010001 & color;
      matrix->displaybuffer[baseCathode + 2] = 0;
      break;
    case 6:
      matrix->displaybuffer[baseCathode] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 1] = B00110011 & color;
      matrix->displaybuffer[baseCathode + 2] = 0;
      break;
    case 7:
      matrix->displaybuffer[baseCathode] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 1] = B01110111 & color;
      matrix->displaybuffer[baseCathode + 2] = 0;
      break;
    case 8:
      matrix->displaybuffer[baseCathode] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 1] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 2] = 0;
      break;
    case 9:
      matrix->displaybuffer[baseCathode] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 1] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 2] = B00010001 & color;
      break;
    case 10:
      matrix->displaybuffer[baseCathode] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 1] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 2] = B00110011 & color;
      break;
    case 11:
      matrix->displaybuffer[baseCathode] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 1] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 2] = B01110111 & color;
      break;
    case 12:
      matrix->displaybuffer[baseCathode] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 1] = B11111111 & color;
      matrix->displaybuffer[baseCathode + 2] = B11111111 & color;
      break;
    default:
      break;
  }  
  
  matrix->writeDisplay();
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
#define LED_GREEN  B11110000
#define LED_RED    B00001111
#define LED_YELLOW B11111111

uint8_t numbers[][3] = {
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
    { B11111111, B11111111, B11111111 }
};
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
