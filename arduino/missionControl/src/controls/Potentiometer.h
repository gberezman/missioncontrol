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

    static const int numReadings = 10;
    int readings[numReadings];
    int currentReadingIndex = 0;
    int averageReading = 0;
    int totalReading = 0;
    int actualReadings = 0;
};

#endif
