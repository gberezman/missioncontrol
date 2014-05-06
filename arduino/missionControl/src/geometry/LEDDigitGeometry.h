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

LEDDigit DIGITS[] = {
  // ATTITUDE
  // LEDDigit( "Pitch0", &matrixA, 0, 0 ),
  // LEDDigit( "Pitch1", &matrixA, 1, 0 ),
  // LEDDigit( "Pitch2", &matrixA, 2, 0 ),
  // LEDDigit( "Yaw0",   &matrixA, 0, 8 ),
  // LEDDigit( "Yaw1",   &matrixA, 1, 8 ),
  // LEDDigit( "Yaw2",   &matrixA, 2, 8 ),
  // LEDDigit( "Roll0",  &matrixA, 3, 0 ),
  // LEDDigit( "Roll1",  &matrixA, 4, 0 ),
  // LEDDigit( "Roll2",  &matrixA, 5, 0 ),

  // SURGEON
  LEDDigit( "IHR0", IHR0 )
  // LEDDigit( "IHR1", &matrixD, 2, 0 ),
  // LEDDigit( "IHR2", &matrixD, 3, 0 ),
  // LEDDigit( "AHR0", &matrixD, 1, 8 ),
  // LEDDigit( "AHR1", &matrixD, 2, 8 ),
  // LEDDigit( "AHR2", &matrixD, 3, 8 ),
  // LEDDigit( "ABR0", &matrixD, 4, 0 ),
  // LEDDigit( "ABR1", &matrixD, 5, 0 ),
  // LEDDigit( "ABR2", &matrixD, 6, 0 )
};

// MissionClock (?)

#endif
