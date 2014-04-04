#include <Wire.h>
#include "comm/SerialCommand.h"
#include "controls/Adafruit_LEDBackpack.h"
#include "controls/LED.h"
#include "controls/LEDMeter.h"
#include "controls/LEDDigit.h"
#include "controls/Potentiometer.h"
#include "controls/Expanders.h"
#include "geometry/LEDGeometry.h"
#include "geometry/LEDMeterGeometry.h"
#include "geometry/PotentiometerGeometry.h"
#include "geometry/LEDDigitGeometry.h"

#include "geometry/ExpanderGeometry.h"

/*
From Geometry files:
    Potentiometer potentiometers[];
    LEDMeter meters[];
    LEDDigit digits[];
    LED leds[];
*/

Adafruit_LEDBackpack matrixA;
Adafruit_LEDBackpack matrixB;
Adafruit_LEDBackpack matrixC;
Adafruit_LEDBackpack matrixD;
Adafruit_LEDBackpack matrixE;

Adafruit_LEDBackpack* matrices[] = {
    &matrixA
};

Expanders expanders( SWITCH_EXPANDERS );

SerialCommand serialCommand;

void setup() {
  Serial.begin(115200);

  Wire.begin();

  initializeMatrices();
  expanders.initialize();

  clearDigits();
  clearLEDs();

  serialCommand.addCommand("Meter", setMeter);
  serialCommand.addCommand("LED", setLED);
  serialCommand.addCommand("Digit", setDigit);
}

void initializeMatrices() {
  for( int i = 0; i < sizeof( matrices ) / sizeof( Adafruit_LEDBackpack ); i++ )
    initializeLEDMatrix( matrices[i], 0x70 + i);
}

void initializeLEDMatrix(Adafruit_LEDBackpack* matrix, uint8_t address) {
  matrix->begin( address );
  matrix->clear();  
  matrix->writeDisplay();
}

void clearDigits() {
  for( int i = 0; i < sizeof( digits ) / sizeof( LEDDigit ); i++ ) 
    digits[i].clear();
}

void clearLEDs() {
  for( int i = 0; i < sizeof( leds ) / sizeof( LED ); i++ ) 
    leds[i].off();
}

void loop() {
  expanders.scan();

  expanders.sendSwitchStates();

  scanPots();
  
  sendPotStates();

  serialCommand.readSerial();
}

void scanPots() {
  for( int i = 0; i < sizeof( potentiometers ) / sizeof( Potentiometer ); i++ ) {
    potentiometers[i].scan();
    delay(2); // recommended pause when accessing analog pins
  }
}

void sendPotStates() {
  for( int i = 0; i < sizeof( potentiometers ) / sizeof( Potentiometer ); i++ ) 
    if( potentiometers[i].hasChanged() )
      potentiometers[i].sendToSerial();
}

void setMeter() {
  char* meterLabel = serialCommand.next();
  char* value = serialCommand.next();

  if( meterLabel != NULL && value != NULL )
    setMeter( meterLabel, atoi( value ) );
}

void setMeter( char* meterLabel, int graphSetting ) {
  LEDMeter* meter = findLEDMeter( meterLabel );
  if( meter != NULL )
    meter->setBars( graphSetting );
}

LEDMeter* findLEDMeter( char* meterLabel ) {
  for( int i = 0; i < sizeof( meters ) / sizeof( LEDMeter ); i++ ) 
    if( strcmp( meterLabel, meters[i].getLabel() ) == 0 ) 
        return &meters[i];
}

void setLED() {
  char* ledLabel = serialCommand.next();
  char* value = serialCommand.next();

  if( ledLabel != NULL && value != NULL ) {
    LED* led = findLED( ledLabel );
    if( led != NULL ) {
      bool isOn = strcmp( value, "on" ) == 0;
      led->set( isOn );
    }
  }
}

LED* findLED( char* ledLabel ) {
  for( int i = 0; i < sizeof( leds ) / sizeof( LED ); i++ ) 
    if( strcmp( ledLabel, leds[i].getLabel() ) == 0 ) 
        return &leds[i];
}

void setDigit() {
  char* digitLabel = serialCommand.next();
  char* value = serialCommand.next();

  if( digitLabel != NULL && value != NULL )
      setDigit( digitLabel, atoi( value ) );
}

void setDigit( char* digitLabel, int digit ) {
  LEDDigit* led = findDigitLED( digitLabel );
  if( led != NULL )
      led->setDigit( digit );
}

LEDDigit* findDigitLED( char* digitLabel ) {
  for( int i = 0; i < sizeof( digits ) / sizeof( LEDDigit ); i++ ) 
    if( strcmp( digitLabel, digits[i].getLabel() ) == 0 ) 
      return &digits[i];
}
