#include <Wire.h>
#include "Potentiometer.h"
#include "Arduino.h"

Potentiometer::Potentiometer( uint8_t _potId, uint8_t _analogPin ) {
  potId = _potId;
  pin = _analogPin;
}

uint8_t Potentiometer::id( void ) {
  return potId;
}

void Potentiometer::scan( void ) {
  previousState = currentState;
  currentState = map( analogRead(pin), 3, 1020, 0, 12 );
}

uint8_t Potentiometer::reading( void ) {
  return currentState;
}

bool Potentiometer::hasChanged( void ) {
  return previousState != currentState;
}
