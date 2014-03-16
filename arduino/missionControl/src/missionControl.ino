#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
#include "LEDMeter.h"
#include "SwitchExpander.h"
#include "SerialCommand.h"

SerialCommand serialCommand;

SwitchExpander exp0(0);
// SwitchExpander exp1(1);
// SwitchExpander exp2(2);
// SwitchExpander exp3(3);

Adafruit_LEDBackpack matrixA;
// Adafruit_LEDBackpack matrixB;
// Adafruit_LEDBackpack matrixC;
// Adafruit_LEDBackpack matrixD;
// Adafruit_LEDBackpack matrixE;

uint8_t prevPotStates[1];
uint8_t currPotStates[1];
  
LEDMeter o2meter = LEDMeter(&matrixA, 0, 0, TWELVE_BAR_DIAL_COLORS);

void setup() {
  Serial.begin(115200);
  
  Wire.begin();

  initializeLEDMatrix( matrixA, 0x70 );
  // initializeLEDMatrix( matrixB, 0x71 );
  // initializeLEDMatrix( matrixC, 0x72 );
  // initializeLEDMatrix( matrixD, 0x73 );
  // initializeLEDMatrix( matrixE, 0x74 );

  serialCommand.addCommand("Meter", setMeter);
}

void initializeLEDMatrix(Adafruit_LEDBackpack matrix, uint8_t address) {
  matrixA.begin( address );
  matrix.clear();  
  matrix.writeDisplay();
}

void loop() {
  scanSwitches();

  sendSwitchStates();

  scanPots();
  
  sendPotStates();

  serialCommand.readSerial();
}

void scanSwitches() {
  exp0.scanSwitches();
  // exp1.scanSwitches();
  // exp2.scanSwitches();
  // exp3.scanSwitches();
}

void sendSwitchStates() {
  sendSwitchStatesToSerial(exp0);
  // sendSwitchStatesToSerial(exp1);
  // sendSwitchStatesToSerial(exp2);
  // sendSwitchStatesToSerial(exp3);
}

void sendSwitchStatesToSerial(SwitchExpander exp) {
  for( int pin = 0; pin < NUM_EXPANDER_PINS; pin++ ) {
    if( exp.wasPinTurnedOn( pin ) ) {
      Serial.print( "S " );
      Serial.print( exp.getPinId(pin) );
      Serial.print( " True\n" );
    }
    else if ( exp.wasPinTurnedOff( pin ) ) {
      Serial.print( "S " );
      Serial.print( exp.getPinId(pin) );
      Serial.print( " False\n" );
    }
  }
}

void scanPots() {
  for( int pot = 0; pot < sizeof(currPotStates)/sizeof(uint8_t); pot++ )
    prevPotStates[pot] = currPotStates[pot];
    
  currPotStates[0] = map( analogRead(7), 3, 1020, 0, 12 );
}

void sendPotStates() {
  for( int pot = 0; pot < sizeof(currPotStates)/sizeof(uint8_t); pot++ ) {
    if( currPotStates[pot] != prevPotStates[pot] ) {
      Serial.print( "P " );
      Serial.print( pot );
      Serial.print( " " );
      Serial.print( currPotStates[pot] );
      Serial.print( "\n" );
    }
  }
}

void setMeter() {
  char* meterLabel = serialCommand.next();
  if( meterLabel != NULL )
    sm( meterLabel );
}

void sm(char* meterLabel) {
  char* value = serialCommand.next();
  if( value != NULL ) {
    int graphSetting = atoi( value );
    LEDMeter* meter = getMeter( meterLabel );
    meter->setBars( graphSetting );
  }
}

LEDMeter* getMeter( char* meterLabel ) {
  if( strcmp( meterLabel, "O2" ) == 0 )
    return &o2meter;
}
