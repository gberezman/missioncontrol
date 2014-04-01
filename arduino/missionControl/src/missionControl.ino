#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
#include "LEDMeter.h"
#include "Potentiometer.h"
#include "SwitchExpander.h"
#include "SerialCommand.h"
#include "LED.h"

SerialCommand serialCommand;

// index of switch corresponds to I/O pin of I/O Expander

char* exp0Switches[16] = {
  // Control 
  "DockingProbe",
  "GlycolPump",
  "SCEPower",
  "WasteDump",
  "CabinFan",
  "H2OFlow",
  "IntLights",
  "SuitComp",

  // Abort
  "ArmAbort",
  "Abort",

  "unused",
  "unused",
  "unused",
  "unused",
  "unused",
  "unused"
};

char* exp1Switches[16] = {
  // Booster
  "SPS",
  "TEI",
  "TLI",
  "S-IC",
  "S-II",
  "S-iVB",
  "M-I",
  "M-II",
  "M-III"

  // C&WS
  "Power",
  "Mode",
  "Lamp",
  "Ack",

  // CAPCOM
  "PTT",

  "unused",
  "unused"
};

char* exp2Switches[16] = {
  // Event Sequence
  "ES1",
  "ES2",
  "ES3",
  "ES4",
  "ES5",
  "ES6",
  "ES7",
  "ES8",
  "ES9",
  "ES10",
  "unused",
  "unused",
  "unused",
  "unused",
  "unused",
  "unused"
};

char* exp3Switches[16] = {
  // Cryogenics
  "O2Fan",
  "H2Fan",
  "Pumps",
  "Heat",

  // Pyrotechnics
  "MainDeploy",
  "CSM/LVDeploy",
  "SM/CMDeploy",
  "DrogueDeploy",
  "CanardDeploy",
  "ApexCoverJettsn",
  "LesMotorFire",

  "unused",
  "unused",
  "unused",
  "unused",
  "unused"
};

SwitchExpander exp0(0, exp0Switches);
SwitchExpander exp1(1, exp1Switches);
SwitchExpander exp2(2, exp2Switches);
SwitchExpander exp3(3, exp3Switches);

Potentiometer potentiometers[] = { 
  // CAPCOM
  Potentiometer( "Speaker",    0 ),
  Potentiometer( "Headset",    1 ),

  // EECOM
  Potentiometer( "Voltage",    2 ),
  Potentiometer( "Current",    3 ),
  Potentiometer( "Resistance", 4 ),
  Potentiometer( "O2Flow",     5 ),

  // INCO
  Potentiometer( "AntPitch",   6 ),
  Potentiometer( "AntYaw",     7 )
};

Adafruit_LEDBackpack matrixA;
Adafruit_LEDBackpack matrixB;
Adafruit_LEDBackpack matrixC;
Adafruit_LEDBackpack matrixD;
Adafruit_LEDBackpack matrixE;

LEDMeter meters[] = { 
  // CRYOGENICS
  LEDMeter( "O2Pressure", &matrixC, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "H2Pressure", &matrixC, 0, 8, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "O2Qty",      &matrixC, 3, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "H2Qty",      &matrixC, 3, 8, TWELVE_BAR_DIAL_COLORS ),

  // INCO
  LEDMeter( "Signal1",    &matrixD, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "Signal2",    &matrixD, 0, 8, TWELVE_BAR_DIAL_COLORS ),

  // EECOM
  LEDMeter( "Current",    &matrixE, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "O2",         &matrixE, 0, 8, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "Voltage",    &matrixE, 3, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "Resistance", &matrixE, 3, 8, TWELVE_BAR_DIAL_COLORS ),
};

// NumericLED numerics[] = {
  // ATTITUDE
  // NumericLED
  // Pitch (3), A, 0-3, 0-7
  // Yaw (3),   A, 0-3, 8-15
  // Roll (3),  A, 4-5, 0-7

  // SURGEON
  // IHR (3),  D, 1-4, 0-7
  // AHR (3),  D, 1-4, 8-15
  // ABR (3),  D, 5-7, 0-7
// };

// MissionClock (?)

LED leds[] = {
  // PANEL1
  LED( "1",            &matrixB, 0, 0 ),
  LED( "2",            &matrixB, 0, 1 ),
  LED( "3",            &matrixB, 0, 2 ),
  LED( "4",            &matrixB, 0, 3 ),
  LED( "5",            &matrixB, 0, 4 ),
  LED( "6",            &matrixB, 0, 5 ),
  LED( "7",            &matrixB, 0, 6 ),
  LED( "8",            &matrixB, 0, 7 ),
  LED( "9",            &matrixB, 0, 8 ),
  LED( "10",           &matrixB, 0, 9 ),
  LED( "11",           &matrixB, 0, 10 ),
  LED( "12",           &matrixB, 0, 11 ),
  LED( "13",           &matrixB, 0, 12 ),
  LED( "14",           &matrixB, 0, 13 ),
  LED( "15",           &matrixB, 0, 14 ),
  LED( "16",           &matrixB, 0, 15 ),
  LED( "17",           &matrixB, 1, 0 ),
  LED( "18",           &matrixB, 1, 1 ),

  // CONTROL
  LED( "CabinFan",     &matrixB, 3, 0 ),
  LED( "H2OFlow",      &matrixB, 3, 1 ),
  LED( "Lights",       &matrixB, 3, 2 ),
  LED( "SuitComp",     &matrixB, 3, 3 ),
  LED( "DockingProbe", &matrixB, 3, 4 ),
  LED( "GlycolPump",   &matrixB, 3, 5 ),
  LED( "SCEPower",     &matrixB, 3, 6 ),
  LED( "WasteDump",    &matrixB, 3, 7 ),

  // PANEL2
  LED( "1",            &matrixD, 5, 8 ),
  LED( "2",            &matrixD, 5, 9 ),
  LED( "3",            &matrixD, 5, 10 ),
  LED( "4",            &matrixD, 5, 11 ),
  LED( "5",            &matrixD, 5, 12 ),
  LED( "6",            &matrixD, 5, 13 ),
  LED( "7",            &matrixD, 5, 14 ),
  LED( "8",            &matrixD, 5, 15 ),
  LED( "9",            &matrixD, 6, 8 ),
  LED( "10",           &matrixD, 6, 9 ),
  LED( "11",           &matrixD, 6, 10 ),
  LED( "12",           &matrixD, 6, 11 ),
  LED( "13",           &matrixD, 6, 12 ),
  LED( "14",           &matrixD, 6, 13 ),
  LED( "15",           &matrixD, 6, 14 ),
  LED( "16",           &matrixD, 6, 15 ),
  LED( "17",           &matrixD, 7, 8 ),
  LED( "18",           &matrixD, 7, 9 ),
    
  // CRYOGENICS
  LED( "O2Fan",        &matrixD, 7, 10 ),
  LED( "H2Fan",        &matrixD, 7, 11 ),
  LED( "Pumps",        &matrixD, 7, 12 ),
  LED( "Heat",         &matrixD, 7, 13 ),

  // EVENT SEQUENCE
  LED( "ES1",          &matrixE, 6, 0 ),
  LED( "ES2",          &matrixE, 6, 1 ),
  LED( "ES3",          &matrixE, 6, 2 ),
  LED( "ES4",          &matrixE, 6, 3 ),
  LED( "ES5",          &matrixE, 6, 4 ),
  LED( "ES6",          &matrixE, 6, 5 ),
  LED( "ES7",          &matrixE, 6, 6 ),
  LED( "ES8",          &matrixE, 6, 7 ),
  LED( "ES9",          &matrixE, 6, 8 ),
  LED( "ES10",         &matrixE, 6, 9 ),

  // C&WS
  LED( "MasterAlarm",  &matrixE, 7, 0 ),

  // ABORT
  LED( "abortSwitch",  &matrixE, 7, 1 )
};

void setup() {
  Serial.begin(115200);
  
  Wire.begin();

  initializeLEDMatrix( &matrixA, 0x70 );
  initializeLEDMatrix( &matrixB, 0x71 );
  initializeLEDMatrix( &matrixC, 0x72 );
  initializeLEDMatrix( &matrixD, 0x73 );
  initializeLEDMatrix( &matrixE, 0x74 );

  serialCommand.addCommand("Meter", setMeter);
  serialCommand.addCommand("LED", setLED);

  forceInitialSwitchStateTransmission();
}

void initializeLEDMatrix(Adafruit_LEDBackpack* matrix, uint8_t address) {
  matrix->begin( address );
  matrix->clear();  
  matrix->writeDisplay();
}

void forceInitialSwitchStateTransmission() {
  scanSwitches();
  invertSwitchStates();
}

void invertSwitchStates() {
  exp0.invert();
  exp1.invert();
  exp2.invert();
  exp3.invert();
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
  exp1.scanSwitches();
  exp2.scanSwitches();
  exp3.scanSwitches();
}

void sendSwitchStates() {
  sendSwitchStatesToSerial(exp0);
  sendSwitchStatesToSerial(exp1);
  sendSwitchStatesToSerial(exp2);
  sendSwitchStatesToSerial(exp3);
}

void sendSwitchStatesToSerial(SwitchExpander exp) {
  for( int pin = 0; pin < NUM_EXPANDER_PINS; pin++ ) {
    if( exp.wasPinTurnedOn( pin ) )
      sendSwitchOn( exp, pin );
    else if ( exp.wasPinTurnedOff( pin ) ) 
      sendSwitchOff( exp, pin );
  }
}

void sendSwitchOn( SwitchExpander exp, int pin ) {
  Serial.print( "S " );
  Serial.print( exp.getPinId(pin) );
  Serial.print( " True\n" );
}

void sendSwitchOff( SwitchExpander exp, int pin ) {
  Serial.print( "S " );
  Serial.print( exp.getPinId(pin) );
  Serial.print( " False\n" );
}

void scanPots() {
  for( int i = 0; i < sizeof( potentiometers ) / sizeof( Potentiometer ); i++ ) 
    potentiometers[i].scan();
}

void sendPotStates() {
  for( int i = 0; i < sizeof( potentiometers ) / sizeof( Potentiometer ); i++ ) 
    if( potentiometers[i].hasChanged() )
        sendPotState( &potentiometers[i] );
}

void sendPotState( Potentiometer* pot ) {
  Serial.print( "P " );
  Serial.print( pot->id() );
  Serial.print( " " );
  Serial.print( pot->reading() );
  Serial.print( "\n" );
}

void setMeter() {
  char* meterLabel = serialCommand.next();
  char* value = serialCommand.next();

  if( meterLabel != NULL && value != NULL )
    setMeter( meterLabel, atoi( value ) );
}

void setMeter( char* meterLabel, int graphSetting ) {
  for( int i = 0; i < sizeof( meters ) / sizeof( LEDMeter ); i++ ) {
    if( strcmp( meterLabel, meters[i].getLabel() ) == 0 ) {
      meters[i].setBars( graphSetting );
      break;
    }
  } 
}

void setLED() {
    char* ledLabel = serialCommand.next();
    char* value = serialCommand.next();

    if( ledLabel != NULL && value != NULL ) {
        bool isOn = strcmp( value, "on" ) == 0;
        setLED( ledLabel, isOn );
    }
}

void setLED( char* ledLabel, bool isOn ) {
  for( int i = 0; i < sizeof( leds ) / sizeof( LED ); i++ ) {
    if( strcmp( ledLabel, leds[i].getLabel() ) == 0 ) {
      if( isOn )
        leds[i].on();
      else
        leds[i].off();
      break;
    }
  } 
}
