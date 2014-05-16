#include <Wire.h>
#include "comm/SerialCommand.h"
#include "controls/Adafruit_LEDBackpack.h"
#include <math.h>

#include "controls/Expanders.h"
#include "controls/Potentiometers.h"
#include "controls/MultiMeter.h"
#include "geometry/LEDCollection.h"
#include "geometry/MeterCollection.h"
#include "geometry/NumberCollection.h"

Adafruit_LEDBackpack matrixA;
Adafruit_LEDBackpack matrixB;
Adafruit_LEDBackpack matrixC;
Adafruit_LEDBackpack matrixD;
Adafruit_LEDBackpack matrixE;

Adafruit_LEDBackpack* matrices[] = {
    &matrixA, 
    &matrixB,
    &matrixC,
    &matrixD
};

Expanders expanders;
Potentiometers pots;
LEDCollection leds;

MeterCollection meters;
NumberCollection numbers;
MultiMeter inco;

SerialCommand serialCommand;

void setup() {
  Serial.begin(115200);

  Wire.begin();

  initializeMatrices();
  expanders.initialize();

  inco.setMeters( meters.getMeter( "Signal1" ), meters.getMeter( "Signal2" ) );

  leds.enableAll();
  numbers.testAll();
  meters.testAll();
  inco.test();

  delay( 1000 );

  leds.disableAll();
  numbers.clearAll();
  meters.clearAll();
  inco.clear();

  serialCommand.addCommand("M", setMeter);
  serialCommand.addCommand("L", setLED);
  serialCommand.addCommand("N", setNumber);
  serialCommand.addCommand("I", setInco);
}

void initializeMatrices() {
  for( int i = 0; i < sizeof( matrices ) / sizeof( Adafruit_LEDBackpack* ); i++ )
    initializeLEDMatrix( matrices[i], 0x70 + i);
}

void initializeLEDMatrix(Adafruit_LEDBackpack* matrix, uint8_t address) {
  matrix->begin( address );
  matrix->setBrightness( 8 );
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
  LEDMeter* meter = meters.getMeter( meterLabel );
  if( meter != NULL )
    meter->setBars( graphSetting );
}

void setInco() {
  char* low = serialCommand.next();
  char* high = serialCommand.next();

  if( low != NULL && high != NULL )
    inco.enableRange( atoi( low ), atoi( high ) );
}

void setLED() {
  char* ledLabel = serialCommand.next();
  char* value = serialCommand.next();

  if( ledLabel != NULL && value != NULL ) {
    LED* led = leds.getLed( ledLabel );
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
  LEDNumber* number = numbers.getNumber( label );
  if( number != NULL )
      number->set( value );
}
