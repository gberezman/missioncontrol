#include <Wire.h>
#include "Potentiometer.h"
#include "Arduino.h"
#include <math.h>

Potentiometer::Potentiometer( char* _potId, uint8_t _analogPin ) {
  potId = _potId;
  pin = _analogPin;
}

char* Potentiometer::id( void ) {
  return potId;
}

void Potentiometer::scan( void ) {
  actualReadings++;
  totalReading = totalReading - readings[currentReadingIndex];
  readings[currentReadingIndex] = map( analogRead(pin), 2, 1020, 0, 12 );
  totalReading = totalReading + readings[currentReadingIndex];
  currentReadingIndex += 1;
  if( currentReadingIndex >= numReadings )
  currentReadingIndex = 0;
  averageReading = totalReading / min( numReadings, actualReadings );

  previousState = currentState;
  currentState = averageReading;
}

uint8_t Potentiometer::reading( void ) {
  return currentState;
}

bool Potentiometer::hasChanged( void ) {
  return previousState != currentState;
}

void Potentiometer::sendToSerial( void ) {
  Serial.print( "P " );
  Serial.print( id() );
  Serial.print( " " );
  Serial.print( reading() );
  Serial.print( "\n" );
}
