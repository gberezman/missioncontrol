#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
#include "LEDMeter.h"
#include "SwitchExpander.h"

SwitchExpander exp0(0);
// SwitchExpander exp1(1);
// SwitchExpander exp2(2);
// SwitchExpander exp3(3);

Adafruit_LEDBackpack matrixA = Adafruit_LEDBackpack();
// Adafruit_LEDBackpack matrixB;
// Adafruit_LEDBackpack matrixC;
// Adafruit_LEDBackpack matrixD;
// Adafruit_LEDBackpack matrixE;

uint8_t prevPotStates[1];
uint8_t currPotStates[1];
uint8_t meterStates[1];
  
LEDMeter o2meter = LEDMeter(&matrixA, 0, 0, TWELVE_BAR_DIAL_COLORS);

void setup() {
  Serial.begin(115200);
  
  Wire.begin();

  initializeLEDMatrix( matrixA, 0x70 );
  // initializeLEDMatrix( matrixB, 0x71 );
  // initializeLEDMatrix( matrixC, 0x72 );
  // initializeLEDMatrix( matrixD, 0x73 );
  // initializeLEDMatrix( matrixE, 0x74 );
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

  scanSerial();

  updateLEDs();
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
  for( uint8_t pin = 0; pin < NUM_EXPANDER_PINS; pin++ ) {
    if( exp.isPinTurnedOn( pin ) )
      Serial.write( exp.getPinId(pin) + 128 );
    else if ( exp.isPinTurnedOff( pin ) )
      Serial.write( exp.getPinId(pin) );
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
      Serial.write( pot | B01000000 );
      Serial.write( currPotStates[pot] | B11000000 );
    }
  }
}

void scanSerial() {
  if( Serial.available() ) {
    while( Serial.available() ) {
      uint8_t value = Serial.read();
      meterStates[0] = value;
    }
  }
}

void updateLEDs() {
  o2meter.setBars(meterStates[0]);
}
