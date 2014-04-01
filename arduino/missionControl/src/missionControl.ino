#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
#include "LEDMeter.h"
#include "Potentiometer.h"
#include "SwitchExpander.h"
#include "SerialCommand.h"

SerialCommand serialCommand;

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
  "PTT"

  "unused",
  "unused"
};

SwitchExpander exp0(0, exp0Switches);
// SwitchExpander exp1(1, exp1Switches);
// SwitchExpander exp2(2, exp2Switches);
// SwitchExpander exp3(3, exp3Switches);

Adafruit_LEDBackpack matrixA;
Adafruit_LEDBackpack matrixB;
Adafruit_LEDBackpack matrixC;
Adafruit_LEDBackpack matrixD;
Adafruit_LEDBackpack matrixE;

#define o2MeterBaseCathodePin 0
#define o2MeterBaseAnodePin 0
LEDMeter o2meter = LEDMeter( &matrixA, "O2", o2MeterBaseCathodePin, o2MeterBaseAnodePin, TWELVE_BAR_DIAL_COLORS );

#define voltageMeterBaseCathodePin 0
#define voltageMeterBaseAnodePin 0
LEDMeter voltageMeter = LEDMeter( &matrixB, "Voltage", voltageMeterBaseAnodePin, voltageMeterBaseAnodePin, TWELVE_BAR_DIAL_COLORS );

LEDMeter* meters[] = { &o2meter, &voltageMeter };

int voltagePotPin = 0;
Potentiometer voltagePot = Potentiometer( "Voltage", voltagePotPin );

void setup() {
  Serial.begin(115200);
  
  Wire.begin();

  initializeLEDMatrix( &matrixA, 0x70 );
  initializeLEDMatrix( &matrixB, 0x71 );
  // initializeLEDMatrix( &matrixC, 0x72 );
  // initializeLEDMatrix( &matrixD, 0x73 );
  // initializeLEDMatrix( &matrixE, 0x74 );

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
  // exp1.invert();
  // exp2.invert();
  // exp3.invert();
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
  // exp1.scanSwitches();
  // exp2.scanSwitches();
  // exp3.scanSwitches();
}

void sendSwitchStates() {
  sendSwitchStatesToSerial(exp0);
  // sendSwitchStatesToSerial(exp1);
  // sendSwitchStatesToSerial(exp2);
  // sendSwitchStatesToSerial(exp3);
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
  voltagePot.scan();
}

void sendPotStates() {
  sendPotStateIfChanged( &voltagePot );
}

void sendPotStateIfChanged( Potentiometer* pot ) {
  if( pot->hasChanged() ) {
    Serial.print( "P " );
    Serial.print( pot->id() );
    Serial.print( " " );
    Serial.print( pot->reading() );
    Serial.print( "\n" );
  }
}

void setMeter() {
  char* meterLabel = serialCommand.next();
  char* value = serialCommand.next();

  if( meterLabel != NULL && value != NULL )
    setMeter( meterLabel, atoi( value ) );
}

void setMeter( char* meterLabel, int graphSetting ) {
  for( int i = 0; i < sizeof( meters ) / sizeof( LEDMeter* ); i++ ) {
    if( strcmp( meterLabel, meters[i]->getLabel() ) == 0 ) {
      meters[i]->setBars( graphSetting );
      break;
    }
  } 
}
