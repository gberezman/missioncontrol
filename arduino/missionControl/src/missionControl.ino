#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
#include "LEDMeter.h"
#include "Potentiometer.h"
#include "SwitchExpander.h"
#include "SerialCommand.h"
#include "LED.h"
#include "LEDDigit.h"

SerialCommand serialCommand;

// index of switch corresponds to I/O pin of I/O Expander

char* exp0Switches[16] = {
  // CONTROL
  "DockingProbe",
  "GlycolPump",
  "SCEPower",
  "WasteDump",
  "CabinFan",
  "H2OFlow",
  "IntLights",
  "SuitComp",

  // ABORT
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
  // BOOSTER
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
  // EVENT SEQUENCE
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
  // CRYOGENICS
  "O2Fan",
  "H2Fan",
  "Pumps",
  "Heat",

  // PYROTECHNICS
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

SwitchExpander expanders[] = {
  SwitchExpander(0, exp0Switches),
  // SwitchExpander(1, exp1Switches),
  // SwitchExpander(2, exp2Switches),
  // SwitchExpander(3, exp3Switches)
};

Potentiometer potentiometers[] = { 
  // CAPCOM
  Potentiometer( "Speaker",    A0 ),
  // Potentiometer( "Headset",    A1 ),

  // ABORT
  // Potentiometer( "AbortMode",  A2 ),

  // EECOM
  // Potentiometer( "Voltage",    A3 ),
  // Potentiometer( "Current",    A4 ),
  // Potentiometer( "Resistance", A5 ),
  // Potentiometer( "O2Flow",     A6 ),

  // INCO
  // Potentiometer( "AntPitch",   A7 ),
  // Potentiometer( "AntYaw",     A8 ),
  // Potentiometer( "Tune",       A9 ),
  // Potentiometer( "Beam",       A10 )
};

Adafruit_LEDBackpack matrixA;
// Adafruit_LEDBackpack matrixB;
// Adafruit_LEDBackpack matrixC;
// Adafruit_LEDBackpack matrixD;
// Adafruit_LEDBackpack matrixE;

LEDMeter meters[] = { 
  // CRYOGENICS
  // LEDMeter( "O2Pressure", &matrixC, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  // LEDMeter( "H2Pressure", &matrixC, 0, 8, TWELVE_BAR_DIAL_COLORS ),
  // LEDMeter( "O2Qty",      &matrixC, 3, 0, TWELVE_BAR_DIAL_COLORS ),
  // LEDMeter( "H2Qty",      &matrixC, 3, 8, TWELVE_BAR_DIAL_COLORS ),

  // INCO
  // LEDMeter( "Signal1",    &matrixD, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  // LEDMeter( "Signal2",    &matrixD, 0, 8, TWELVE_BAR_DIAL_COLORS ),

  // EECOM
  // LEDMeter( "Voltage",    &matrixE, 0, 0, TWELVE_BAR_DIAL_COLORS ),
  // LEDMeter( "Current",    &matrixE, 0, 8, TWELVE_BAR_DIAL_COLORS ),
  // LEDMeter( "Resistance", &matrixE, 3, 0, TWELVE_BAR_DIAL_COLORS ),
  // LEDMeter( "O2Flow",     &matrixE, 3, 8, TWELVE_BAR_DIAL_COLORS ),
};

LEDDigit digits[] = {
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
  // LEDDigit( "IHR0", &matrixD, 1, 0 ),
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

void setup() {
  Serial.begin(115200);

  Wire.begin();

  initializeLEDMatrix( &matrixA, 0x70 );
  // initializeLEDMatrix( &matrixB, 0x71 );
  // initializeLEDMatrix( &matrixC, 0x72 );
  // initializeLEDMatrix( &matrixD, 0x73 );
  // initializeLEDMatrix( &matrixE, 0x74 );

  serialCommand.addCommand("Meter", setMeter);
  serialCommand.addCommand("LED", setLED);
  serialCommand.addCommand("Digit", setDigit);

  clearDigits();
  clearLEDs();
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

void clearDigits() {
  for( int i = 0; i < sizeof( digits ) / sizeof( LEDDigit ); i++ ) 
    digits[i].clear();
}

void clearLEDs() {
  for( int i = 0; i < sizeof( leds ) / sizeof( LED ); i++ ) 
    leds[i].off();
}

void invertSwitchStates() {
  for( int i = 0; i < sizeof(expanders)/sizeof(SwitchExpander); i++ )
    expanders[i].invert();
}

void loop() {
  scanSwitches();

  sendSwitchStates();

  scanPots();
  
  sendPotStates();

  serialCommand.readSerial();
}

void scanSwitches() {
  for( int i = 0; i < sizeof(expanders)/sizeof(SwitchExpander); i++ )
    expanders[i].scanSwitches();
}

void sendSwitchStates() {
  for( int i = 0; i < sizeof(expanders)/sizeof(SwitchExpander); i++ )
    sendSwitchStatesToSerial(expanders[i]);
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
  for( int i = 0; i < sizeof( potentiometers ) / sizeof( Potentiometer ); i++ ) {
    potentiometers[i].scan();
    delay(2); // recommended pause when accessing analog pins
  }
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
  LEDMeter* meter = findLEDMeter( meterLabel );
  if( meter != NULL )
    meter->setBars( graphSetting );
}

LEDMeter* findLEDMeter( char* meterLabel ) {
  for( int i = 0; i < sizeof( meters ) / sizeof( LEDMeter ); i++ ) 
    if( strcmp( meterLabel, meters[i].getLabel() ) == 0 ) 
        return &meters[i];
}

void setLED() {
  char* ledLabel = serialCommand.next();
  char* value = serialCommand.next();

  if( ledLabel != NULL && value != NULL ) {
    LED* led = findLED( ledLabel );
    if( led != NULL ) {
      bool isOn = strcmp( value, "on" ) == 0;
      led->set( isOn );
    }
  }
}

LED* findLED( char* ledLabel ) {
  for( int i = 0; i < sizeof( leds ) / sizeof( LED ); i++ ) 
    if( strcmp( ledLabel, leds[i].getLabel() ) == 0 ) 
        return &leds[i];
}

void setDigit() {
  char* digitLabel = serialCommand.next();
  char* value = serialCommand.next();

  if( digitLabel != NULL && value != NULL )
      setDigit( digitLabel, atoi( value ) );
}

void setDigit( char* digitLabel, int digit ) {
  LEDDigit* led = findDigitLED( digitLabel );
  if( led != NULL )
      led->setDigit( digit );
}

LEDDigit* findDigitLED( char* digitLabel ) {
  for( int i = 0; i < sizeof( digits ) / sizeof( LEDDigit ); i++ ) 
    if( strcmp( digitLabel, digits[i].getLabel() ) == 0 ) 
      return &digits[i];
}
