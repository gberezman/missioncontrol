#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
#include "LEDMeter.h"
#include "SwitchExpander.h"

SwitchExpander exp0;
// SwitchExpander exp1;
// SwitchExpander exp2;
// SwitchExpander exp3;

Adafruit_LEDBackpack matrixA = Adafruit_LEDBackpack();
// Adafruit_LEDBackpack matrixB;
// Adafruit_LEDBackpack matrixC;
// Adafruit_LEDBackpack matrixD;
// Adafruit_LEDBackpack matrixE;

uint8_t potStates[1];
  
LEDMeter o2meter = LEDMeter(&matrixA, 0, 0, TWELVE_BAR_DIAL_COLORS);

void setup() {
  Serial.begin(115200);
  
  Wire.begin();

  exp0.initialize(0);
  // exp1.initialize(1);
  // exp2.initialize(2);
  // exp3.initialize(3);

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
  
  potStates[0] = map( analogRead(7), 0, 1023, 0, 12 );  
  
  updateMeters();
}

void scanSwitches() {
  exp0.scanSwitches();
  sendSwitchStates(exp0);
}

void sendSwitchStates(SwitchExpander exp) {
  for( uint8_t pin = 0; pin < NUM_EXPANDER_PINS; pin++ ) {
    if( exp.isPinTurnedOn( pin ) )
      Serial.write( exp.getPinId(pin) + 128 );
    else if ( exp.isPinTurnedOff( pin ) )
      Serial.write( exp.getPinId(pin) );
  }
}

void updateMeters() {
  o2meter.setBars(potStates[0]);
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
*/

