#include <Wire.h>
#include "comm/SerialCommand.h"
#include "controls/Adafruit_LEDBackpack.h"

#include "controls/Expanders.h"
#include "controls/Potentiometers.h"
#include "controls/LEDs.h"
#include "controls/LEDMeters.h"
#include "controls/LEDDigits.h"

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
LEDDigits digits;

SerialCommand serialCommand;

void setup() {
  Serial.begin(115200);

  Wire.begin();

  initializeMatrices();
  expanders.initialize();

  digits.test();
  leds.test();
  delay( 1000 );

  digits.clear();
  leds.clear();

  serialCommand.addCommand("Meter", setMeter);
  serialCommand.addCommand("LED",   setLED);
  serialCommand.addCommand("Digit", setDigit);
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
      bool isOn = strcmp( value, "on" ) == 0;
      led->set( isOn );
    }
  }
}

void setDigit() {
  char* digitLabel = serialCommand.next();
  char* value = serialCommand.next();

  if( digitLabel != NULL && value != NULL )
      setDigit( digitLabel, atoi( value ) );
}

void setDigit( char* digitLabel, int digit ) {
  LEDDigit* led = digits.findLEDDigit( digitLabel );
  if( led != NULL )
      led->setDigit( digit );
}
