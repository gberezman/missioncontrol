#ifndef LEDDIGIT_GEOMETRY_H
#define LEDDIGIT_GEOMETRY_H

#include "../controls/LEDDigit.h"
#include "../controls/Adafruit_LEDBackpack.h"

extern Adafruit_LEDBackpack matrixA;
extern Adafruit_LEDBackpack matrixB;
extern Adafruit_LEDBackpack matrixC;
extern Adafruit_LEDBackpack matrixD;
extern Adafruit_LEDBackpack matrixE;

LED IHR0[] = {
    LED( "top right",    &matrixB, 6, 6 ),
    LED( "bottom right", &matrixB, 2, 6 ),
    LED( "bottom",       &matrixB, 4, 6 ),
    LED( "bottom left",  &matrixB, 7, 6 ),
    LED( "top left",     &matrixB, 0, 6 ),
    LED( "top",          &matrixB, 5, 6 ),
    LED( "middle",       &matrixB, 1, 6 ),
    LED( "point",        &matrixB, 3, 6 )
};

LED IHR1[] = {
    LED( "top right",    &matrixB, 6, 7 ),
    LED( "bottom right", &matrixB, 2, 7 ),
    LED( "bottom",       &matrixB, 4, 7 ),
    LED( "bottom left",  &matrixB, 7, 7 ),
    LED( "top left",     &matrixB, 0, 7 ),
    LED( "top",          &matrixB, 5, 7 ),
    LED( "middle",       &matrixB, 1, 7 ),
    LED( "point",        &matrixB, 3, 7 )
};

LEDDigit DIGITS[] = {
  // SURGEON
  LEDDigit( "IHR0", IHR0 ),
  LEDDigit( "IHR1", IHR1 ),
};

// MissionClock (?)

#endif
