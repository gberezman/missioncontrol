#ifndef LEDMETER_GEOMETRY_H
#define LEDMETER_GEOMETRY_H

#include "../controls/LEDMeter.h"
#include "../controls/Adafruit_LEDBackpack.h"

extern Adafruit_LEDBackpack matrixA;
extern Adafruit_LEDBackpack matrixB;
extern Adafruit_LEDBackpack matrixC;
extern Adafruit_LEDBackpack matrixD;
extern Adafruit_LEDBackpack matrixE;

LEDMeter METERS[] = { 
  // CRYOGENICS
  LEDMeter( "O2Pressure", &matrixC, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "H2Pressure", &matrixC, 0, 8, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "O2Qty",      &matrixC, 3, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "H2Qty",      &matrixC, 3, 8, TWELVE_BAR_DIAL_COLORS )

  // INCO
  // LEDMeter( "Signal1",    &matrixD, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  // LEDMeter( "Signal2",    &matrixD, 0, 8, TWELVE_BAR_DIAL_COLORS ),

  // EECOM
  // LEDMeter( "Voltage",    &matrixE, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  // LEDMeter( "Current",    &matrixE, 0, 8, TWELVE_BAR_DIAL_COLORS ),
  // LEDMeter( "Resistance", &matrixE, 3, 0, TWELVE_BAR_DIAL_COLORS ),
  // LEDMeter( "O2Flow",     &matrixE, 3, 8, TWELVE_BAR_DIAL_COLORS ),
};

#endif
