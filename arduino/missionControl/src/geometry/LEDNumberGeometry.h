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

LED IHR2[] = {
    LED( "top right",    &matrixB, 5, 8 ),
    LED( "bottom right", &matrixB, 2, 8 ),
    LED( "bottom",       &matrixB, 4, 8 ),
    LED( "bottom left",  &matrixB, 7, 8 ),
    LED( "top left",     &matrixB, 0, 8 ),
    LED( "top",          &matrixB, 6, 8 ),
    LED( "middle",       &matrixB, 1, 8 ),
    LED( "point",        &matrixB, 3, 8 )
};

LED AHR0[] = {
    LED( "top right",    &matrixB, 5, 3 ),
    LED( "bottom right", &matrixB, 2, 3 ),
    LED( "bottom",       &matrixB, 4, 3 ),
    LED( "bottom left",  &matrixB, 7, 3 ),
    LED( "top left",     &matrixB, 0, 3 ),
    LED( "top",          &matrixB, 6, 3 ),
    LED( "middle",       &matrixB, 1, 3 ),
    LED( "point",        &matrixB, 3, 3 )
};

LED AHR1[] = {
    LED( "top right",    &matrixB, 5, 4 ),
    LED( "bottom right", &matrixB, 2, 4 ),
    LED( "bottom",       &matrixB, 4, 4 ),
    LED( "bottom left",  &matrixB, 7, 4 ),
    LED( "top left",     &matrixB, 0, 4 ),
    LED( "top",          &matrixB, 6, 4 ),
    LED( "middle",       &matrixB, 1, 4 ),
    LED( "point",        &matrixB, 3, 4 )
};

LED AHR2[] = {
    LED( "top right",    &matrixB, 5, 5 ),
    LED( "bottom right", &matrixB, 2, 5 ),
    LED( "bottom",       &matrixB, 4, 5 ),
    LED( "bottom left",  &matrixB, 7, 5 ),
    LED( "top left",     &matrixB, 0, 5 ),
    LED( "top",          &matrixB, 6, 5 ),
    LED( "middle",       &matrixB, 1, 5 ),
    LED( "point",        &matrixB, 3, 5 )
};

LED ABR0[] = {
    LED( "top right",    &matrixB, 5, 0 ),
    LED( "bottom right", &matrixB, 2, 0 ),
    LED( "bottom",       &matrixB, 4, 0 ),
    LED( "bottom left",  &matrixB, 7, 0 ),
    LED( "top left",     &matrixB, 0, 0 ),
    LED( "top",          &matrixB, 6, 0 ),
    LED( "middle",       &matrixB, 1, 0 ),
    LED( "point",        &matrixB, 3, 0 )
};

LED ABR1[] = {
    LED( "top right",    &matrixB, 5, 1 ),
    LED( "bottom right", &matrixB, 2, 1 ),
    LED( "bottom",       &matrixB, 4, 1 ),
    LED( "bottom left",  &matrixB, 7, 1 ),
    LED( "top left",     &matrixB, 0, 1 ),
    LED( "top",          &matrixB, 6, 1 ),
    LED( "middle",       &matrixB, 1, 1 ),
    LED( "point",        &matrixB, 3, 1 )
};

LED ABR2[] = {
    LED( "top right",    &matrixB, 0, 2 ),
    LED( "bottom right", &matrixB, 2, 2 ),
    LED( "bottom",       &matrixB, 4, 2 ),
    LED( "bottom left",  &matrixB, 7, 2 ),
    LED( "top left",     &matrixB, 5, 2 ),
    LED( "top",          &matrixB, 6, 2 ),
    LED( "middle",       &matrixB, 1, 2 ),
    LED( "point",        &matrixB, 3, 2 )
};

LEDDigit IHR[] = {
  LEDDigit( "IHR0", IHR0 ),
  LEDDigit( "IHR1", IHR1 ),
  LEDDigit( "IHR2", IHR2 )
};

LEDDigit AHR[] = {
  LEDDigit( "AHR0", AHR0 ),
  LEDDigit( "AHR1", AHR1 ),
  LEDDigit( "AHR2", AHR2 )
};

LEDDigit ABR[] = {
  LEDDigit( "ABR0", ABR0 ),
  LEDDigit( "ABR1", ABR1 ),
  LEDDigit( "ABR2", ABR2 )
};

LEDNumber NUMBERS[] = {
  LEDNumber( "ABR", ABR ),
  LEDNumber( "AHR", AHR ),
  LEDNumber( "IHR", IHR )
};

// MissionClock (?)

#endif
