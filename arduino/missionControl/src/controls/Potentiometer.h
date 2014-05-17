#ifndef _POTENTIOMETER_H
#define _POTENTIOMETER_H

#include "Arduino.h"

class Smoother {
  public:
    void record( int value );
    int getValue();
    
  private:
    static const int numReadings = 10;
    int readings[numReadings];
    int index = 0;
    int average = 0;
    int total = 0;
    long count = 0;
};

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
    Smoother smoother;
};

#endif
