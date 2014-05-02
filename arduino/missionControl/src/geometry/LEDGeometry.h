#ifndef LED_GEOMETRY_H
#define LED_GEOMETRY_H

#include "../controls/LED.h"
#include "../controls/Adafruit_LEDBackpack.h"

extern Adafruit_LEDBackpack matrixA;
extern Adafruit_LEDBackpack matrixB;
extern Adafruit_LEDBackpack matrixC;
extern Adafruit_LEDBackpack matrixD;
extern Adafruit_LEDBackpack matrixE;

LED LEDS[] = {
  // PANEL1
  LED( "DrogueChute",     &matrixA, 0, 0 ),
  LED( "MainChute",       &matrixA, 0, 1 ),
  LED( "SPSPress",        &matrixA, 0, 2 ),
  LED( "ACBus1Overload",  &matrixA, 0, 3 ),
  LED( "Ullage",          &matrixA, 1, 0 ),
  LED( "Hatch",           &matrixA, 1, 1 ),
  LED( "ACBus1",          &matrixA, 1, 2 ),
  LED( "SPSRoughEco",     &matrixA, 1, 3 ),
  LED( "Thrust",          &matrixA, 2, 0 ),
  LED( "DockingTarget",   &matrixA, 2, 1 ),
  LED( "ACBus2",          &matrixA, 2, 2 ),
  LED( "CW",              &matrixA, 2, 3 ),
  LED( "FCBusDisscnct",   &matrixA, 3, 0 ),
  LED( "O2FlowHi",        &matrixA, 3, 1 ),
  LED( "SuitComp",        &matrixA, 3, 2 ),
  LED( "SPSFlngTempHi",   &matrixA, 4, 0 ),
  LED( "CrewAlert",       &matrixA, 4, 1 ),
  LED( "ACBus2Overload",  &matrixA, 4, 2 ),

  // CRYOGENICS
  LED( "O2Fan",           &matrixA, 0, 9 ),
  LED( "H2Fan",           &matrixA, 1, 9 ),
  LED( "Pumps",           &matrixA, 2, 9 ),
  LED( "Heat",            &matrixA, 3, 9 ),

  // EVENT SEQUENCE
  LED( "ES1",             &matrixA, 0, 5 ),
  LED( "ES2",             &matrixA, 1, 5 ),
  LED( "ES3",             &matrixA, 2, 5 ),
  LED( "ES4",             &matrixA, 3, 5 ),
  LED( "ES5",             &matrixA, 4, 5 ),
  LED( "ES6",             &matrixA, 0, 6 ),
  LED( "ES7",             &matrixA, 1, 6 ),
  LED( "ES8",             &matrixA, 2, 6 ),
  LED( "ES9",             &matrixA, 3, 6 ),
  LED( "ES10",            &matrixA, 4, 6 )

  // ABORT
  // LED( "ArmAbort",        &matrixB, 0, 9 ),
  // LED( "Abort",           &matrixB, 1, 9 ),

  // C&WS
  // LED( "MasterAlarm",     &matrixB, 0, 10 ),
  // LED( "Ack",             &matrixB, 1, 10 ),

  // PANEL2
  // LED( "BMagTemp1",      &matrixB, 0, 11 ),
  // LED( "PitchGmbl1",     &matrixB, 0, 12 ),
  // LED( "PitchGmbl2",     &matrixB, 0, 13 ),
  // LED( "GlycolTempLow",  &matrixB, 0, 14 ),
  // LED( "SMRCSA",         &matrixB, 0, 15 ),
  // LED( "BMagTemp2",      &matrixB, 1, 11 ),
  // LED( "YawGmbl1",       &matrixB, 1, 12 ),
  // LED( "YawGmbl2",       &matrixB, 1, 13 ),
  // LED( "CMRCS1",         &matrixB, 1, 14 ),
  // LED( "SMRCSB",         &matrixB, 1, 15 ),
  // LED( "CO2PPHi",        &matrixB, 2, 11 ),
  // LED( "HGAntScanLimit", &matrixB, 2, 12 ),
  // LED( "CryoPress",      &matrixB, 2, 13 ),
  // LED( "CMRCS2",         &matrixB, 2, 14 ),
  // LED( "SMRCSC",         &matrixB, 2, 15 ),
  // LED( "SMRCSB",         &matrixB, 3, 11 ),
  // LED( "UplinkActivity", &matrixB, 3, 12 ),
  // LED( "GimbalLock",     &matrixB, 3, 13 ),
    
  // CONTROL
  // LED( "DockingProbe", &matrixD, 6, 8 ),
  // LED( "GlycolPump",   &matrixD, 6, 9 ),
  // LED( "SCEPower",     &matrixD, 6, 10 ),
  // LED( "WasteDump",    &matrixD, 6, 11 ),
  // LED( "CabinFan",     &matrixD, 7, 9 ),
  // LED( "H2OFlow",      &matrixD, 7, 10 ),
  // LED( "Lights",       &matrixD, 7, 11 ),
  // LED( "SuitComp",     &matrixD, 7, 12 )
};

#endif
