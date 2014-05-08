#include <Wire.h>
#include "comm/SerialCommand.h"
#include "controls/Adafruit_LEDBackpack.h"

#include "controls/Expanders.h"
#include "controls/Potentiometers.h"
#include "controls/LEDs.h"
#include "controls/LEDMeters.h"
#include "controls/LEDNumbers.h"

Adafruit_LEDBackpack matrixA;
Adafruit_LEDBackpack matrixB;
Adafruit_LEDBackpack matrixC;
Adafruit_LEDBackpack matrixD;
Adafruit_LEDBackpack matrixE;

Adafruit_LEDBackpack* matrices[] = {
    &matrixA, 
    &matrixB
};

Expanders expanders;
Potentiometers pots;
LEDs leds;
LEDMeters meters;
LEDNumbers numbers;

SerialCommand serialCommand;

void setup() {
  Serial.begin(115200);

  Wire.begin();

  initializeMatrices();
  expanders.initialize();

  leds.test();
  numbers.test();

  delay( 1000 );

  numbers.clear();
  leds.clear();

  serialCommand.addCommand("M", setMeter);
  serialCommand.addCommand("L", setLED);
  serialCommand.addCommand("N", setNumber);
}

void initializeMatrices() {
  for( int i = 0; i < sizeof( matrices ) / sizeof( Adafruit_LEDBackpack* ); i++ )
    initializeLEDMatrix( matrices[i], 0x70 + i);
}

void initializeLEDMatrix(Adafruit_LEDBackpack* matrix, uint8_t address) {
  matrix->begin( address );
  matrix->clear();  
  matrix->writeDisplay();
}

void loop() {
  expanders.scan();

  expanders.sendSwitchStates();

  pots.scan();
  
  pots.sendPotStates();

  serialCommand.readSerial();
}

void setMeter() {
  char* meterLabel = serialCommand.next();
  char* value = serialCommand.next();

  if( meterLabel != NULL && value != NULL )
    setMeter( meterLabel, atoi( value ) );
}

void setMeter( char* meterLabel, int graphSetting ) {
  LEDMeter* meter = meters.findLEDMeter( meterLabel );
  if( meter != NULL )
    meter->setBars( graphSetting );
}

void setLED() {
  char* ledLabel = serialCommand.next();
  char* value = serialCommand.next();

  if( ledLabel != NULL && value != NULL ) {
    LED* led = leds.findLED( ledLabel );
    if( led != NULL ) {
      bool isOn = strcmp( value, "1" ) == 0;
      led->set( isOn );
    }
  }
}

void setNumber() {
  char* label = serialCommand.next();
  char* value = serialCommand.next();

  if( label != NULL && value != NULL )
      setNumber( label, value );
}

void setNumber( char* label, char* value ) {
  LEDNumber* number = numbers.findLEDNumber( label );
  if( number != NULL )
      number->set( value );
}
