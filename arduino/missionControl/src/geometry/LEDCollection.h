#ifndef LED_DEFINITIONS_H
#define LED_DEFINITIONS_H

#include <Arduino.h>
#include "../controls/LED.h"
#include "../controls/Adafruit_LEDBackpack.h"

extern Adafruit_LEDBackpack matrixA;
extern Adafruit_LEDBackpack matrixB;
extern Adafruit_LEDBackpack matrixC;
extern Adafruit_LEDBackpack matrixD;
extern Adafruit_LEDBackpack matrixE;

class LEDCollection {
  public:
    LED* getLed( char* label );
    void enableAll( void );
    void disableAll( void );

  private:
    static LED leds[];
};

#endif
