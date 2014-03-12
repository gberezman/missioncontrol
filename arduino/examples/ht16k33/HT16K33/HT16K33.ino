/*************************************************** 
  This is a library for our I2C LED Backpacks

  Designed specifically to work with the Adafruit LED Matrix backpacks 
  ----> http://www.adafruit.com/products/872
  ----> http://www.adafruit.com/products/871
  ----> http://www.adafruit.com/products/870

  These displays use I2C to communicate, 2 pins are required to 
  interface. There are multiple selectable I2C addresses. For backpacks
  with 2 Address Select pins: 0x70, 0x71, 0x72 or 0x73. For backpacks
  with 3 Address Select pins: 0x70 thru 0x77

  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
#include "Adafruit_GFX.h"

Adafruit_LEDBackpack matrix = Adafruit_LEDBackpack();

void setup() { 
  matrix.begin(0x70);
  matrix.setBrightness(5);
  
  matrix.displaybuffer[0] = _BV(0);
  matrix.displaybuffer[0] |= _BV(1);
  matrix.displaybuffer[0] |= _BV(2);
  matrix.displaybuffer[0] |= _BV(3);
  matrix.displaybuffer[0] |= _BV(4);
  matrix.displaybuffer[0] |= _BV(5);
  matrix.displaybuffer[0] |= _BV(6);
  matrix.displaybuffer[0] |= _BV(7);
  matrix.displaybuffer[1] = _BV(0);
  matrix.displaybuffer[1] |= _BV(1);
  matrix.displaybuffer[1] |= _BV(2);
  matrix.displaybuffer[1] |= _BV(3);
  matrix.displaybuffer[2] = _BV(4);
  matrix.displaybuffer[2] |= _BV(5);
  matrix.displaybuffer[2] |= _BV(6);
  matrix.displaybuffer[2] |= _BV(7);
  
  matrix.writeDisplay();
}

void loop() {
  // matrix.writeDisplay();
  // delay(10);
}
