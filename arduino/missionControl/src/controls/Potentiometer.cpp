#include <Wire.h>
#include "Potentiometer.h"
#include "Arduino.h"
#include <math.h>

Potentiometer::Potentiometer( char* _potId, uint8_t _analogPin, int _limit ) {
  potId = _potId;
  pin = _analogPin;
  limit = _limit;
}

char* Potentiometer::id( void ) {
  return potId;
}

void Potentiometer::scan( void ) {
  // invert the reading
  int reading = limit - map( analogRead(pin), 2, 1020, 0, limit );

  smoother.record( reading );

  previousState = currentState;
  currentState = smoother.getValue();
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

void Smoother::record( int value ) {
  total = total - readings[index];
  readings[index] = value;
  total = total + readings[index];

  if( ++index >= numReadings )
    index = 0;

  average = total / min( numReadings, ++count );
}

int Smoother::getValue( void ) {
  return average;
}
