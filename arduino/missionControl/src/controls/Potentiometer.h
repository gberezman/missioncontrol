#ifndef _POTENTIOMETER_H
#define _POTENTIOMETER_H

#include "Arduino.h"

class Potentiometer {
  public:
    Potentiometer( char* _potId, uint8_t _analogPin );
    void scan( void );
    char* id( void );
    uint8_t reading( void );
    bool hasChanged( void );
    void sendToSerial( void );

  private:
    uint8_t pin;
    char* potId;
    uint8_t currentState;
    uint8_t previousState;
    unsigned long lastPoll = 0;
    int pollFrequency_ms = 100;
};

#endif
