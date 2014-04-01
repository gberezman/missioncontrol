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

Adafruit_LEDBackpack matrixA;
Adafruit_LEDBackpack matrixB;
Adafruit_LEDBackpack matrixC;
Adafruit_LEDBackpack matrixD;
Adafruit_LEDBackpack matrixE;

LEDMeter meters[] = { 
  // EECOM
  LEDMeter( "Current", &matrixA, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "O2", &matrixA, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "Voltage", &matrixB, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "Resistance", &matrixB, 0, 0, TWELVE_BAR_DIAL_COLORS ),

  // CRYOGENICS
  LEDMeter( "O2Pressure", &matrixA, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "H2Pressure", &matrixA, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "O2Qty", &matrixA, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "H2Qty", &matrixA, 0, 0, TWELVE_BAR_DIAL_COLORS ),

  // INCO
  LEDMeter( "Signal1", &matrixA, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  LEDMeter( "Signal2", &matrixA, 0, 0, TWELVE_BAR_DIAL_COLORS )
};

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

// NumericLED numerics[] = {
  // ATTITUDE
  // NumericLED
  // Pitch (3)
  // Yaw (3)
  // Roll (3)

  // SURGEON
  // IHR (3)
  // AHR (3)
  // ABR (3)
// };

// MissionClock (?)

LED leds[] = {
  // ABORT
  LED( "abortSwitch",  &matrixA, 0, 0 ),
    
  // CONTROL
  LED( "CabinFan",     &matrixA, 0, 0),
  LED( "H2OFlow",      &matrixA, 0, 0),
  LED( "Lights",       &matrixA, 0, 0),
  LED( "SuitComp",     &matrixA, 0, 0),
  LED( "DockingProbe", &matrixA, 0, 0),
  LED( "GlycolPump",   &matrixA, 0, 0),
  LED( "SCEPower",     &matrixA, 0, 0),
  LED( "WasteDump",    &matrixA, 0, 0),

  // C&WS
  LED( "MasterAlarm",  &matrixA, 0, 0),

  // EVENT SEQUENCE
  LED( "ES1",          &matrixA, 0, 0),
  LED( "ES2",          &matrixA, 0, 0),
  LED( "ES3",          &matrixA, 0, 0),
  LED( "ES4",          &matrixA, 0, 0),
  LED( "ES5",          &matrixA, 0, 0),
  LED( "ES6",          &matrixA, 0, 0),
  LED( "ES7",          &matrixA, 0, 0),
  LED( "ES8",          &matrixA, 0, 0),
  LED( "ES9",          &matrixA, 0, 0),
  LED( "ES10",         &matrixA, 0, 0),

  // CRYOGENICS
  LED( "O2Fan",        &matrixA, 0, 0),
  LED( "H2Fan",        &matrixA, 0, 0),
  LED( "Pumps",        &matrixA, 0, 0),
  LED( "Heat",         &matrixA, 0, 0)
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
