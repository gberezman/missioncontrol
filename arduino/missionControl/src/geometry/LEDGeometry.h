#ifndef LED_GEOMETRY_H
#define LED_GEOMETRY_H

#include "controls/LED.h"
#include "controls/Adafruit_LEDBackpack.h"

extern Adafruit_LEDBackpack matrixA;
extern Adafruit_LEDBackpack matrixB;
extern Adafruit_LEDBackpack matrixC;
extern Adafruit_LEDBackpack matrixD;
extern Adafruit_LEDBackpack matrixE;

LED leds[] = {
  // PANEL1
  // LED( "1",            &matrixB, 0, 0 ),
  // LED( "2",            &matrixB, 0, 1 ),
  // LED( "3",            &matrixB, 0, 2 ),
  // LED( "4",            &matrixB, 0, 3 ),
  // LED( "5",            &matrixB, 0, 4 ),
  // LED( "6",            &matrixB, 0, 5 ),
  // LED( "7",            &matrixB, 0, 6 ),
  // LED( "8",            &matrixB, 0, 7 ),
  // LED( "9",            &matrixB, 0, 8 ),
  // LED( "10",           &matrixB, 0, 9 ),
  // LED( "11",           &matrixB, 0, 10 ),
  // LED( "12",           &matrixB, 0, 11 ),
  // LED( "13",           &matrixB, 0, 12 ),
  // LED( "14",           &matrixB, 0, 13 ),
  // LED( "15",           &matrixB, 0, 14 ),
  // LED( "16",           &matrixB, 0, 15 ),
  // LED( "17",           &matrixB, 1, 0 ),
  // LED( "18",           &matrixB, 1, 1 ),

  // CONTROL
  // LED( "CabinFan",     &matrixB, 3, 0 ),
  // LED( "H2OFlow",      &matrixB, 3, 1 ),
  // LED( "Lights",       &matrixB, 3, 2 ),
  // LED( "SuitComp",     &matrixB, 3, 3 ),
  // LED( "DockingProbe", &matrixB, 3, 4 ),
  // LED( "GlycolPump",   &matrixB, 3, 5 ),
  // LED( "SCEPower",     &matrixB, 3, 6 ),
  // LED( "WasteDump",    &matrixB, 3, 7 ),

  // PANEL2
  // LED( "1",            &matrixD, 4, 8 ),
  // LED( "2",            &matrixD, 4, 9 ),
  // LED( "3",            &matrixD, 4, 10 ),
  // LED( "4",            &matrixD, 4, 11 ),
  // LED( "5",            &matrixD, 4, 12 ),
  // LED( "6",            &matrixD, 4, 13 ),
  // LED( "7",            &matrixD, 4, 14 ),
  // LED( "8",            &matrixD, 4, 15 ),
  // LED( "9",            &matrixD, 5, 8 ),
  // LED( "10",           &matrixD, 5, 9 ),
  // LED( "11",           &matrixD, 5, 10 ),
  // LED( "12",           &matrixD, 5, 11 ),
  // LED( "13",           &matrixD, 5, 12 ),
  // LED( "14",           &matrixD, 5, 13 ),
  // LED( "15",           &matrixD, 5, 14 ),
  // LED( "16",           &matrixD, 5, 15 ),
  // LED( "17",           &matrixD, 6, 8 ),
  // LED( "18",           &matrixD, 6, 9 ),
    
  // CRYOGENICS
  // LED( "O2Fan",        &matrixD, 7, 0 ),
  // LED( "H2Fan",        &matrixD, 7, 1 ),
  // LED( "Pumps",        &matrixD, 7, 2 ),
  // LED( "Heat",         &matrixD, 7, 3 ),

  // EVENT SEQUENCE
  // LED( "ES1",          &matrixE, 6, 0 ),
  // LED( "ES2",          &matrixE, 6, 1 ),
  // LED( "ES3",          &matrixE, 6, 2 ),
  // LED( "ES4",          &matrixE, 6, 3 ),
  // LED( "ES5",          &matrixE, 6, 4 ),
  // LED( "ES6",          &matrixE, 6, 5 ),
  // LED( "ES7",          &matrixE, 6, 6 ),
  // LED( "ES8",          &matrixE, 6, 7 ),
  // LED( "ES9",          &matrixE, 6, 8 ),
  // LED( "ES10",         &matrixE, 6, 9 ),

  // C&WS
  // LED( "MasterAlarm",  &matrixE, 7, 0 ),

  // ABORT
  // LED( "abortSwitch",  &matrixE, 7, 1 )
};

#endif
