#ifndef _LED_H
#define _LED_H

#include "Adafruit_LEDBackpack.h"

class LED {
  public:
    LED(char* label, Adafruit_LEDBackpack* matrix, uint8_t cathode, uint8_t anode);
    void set( bool turnOn );
    void on( void );
    void stageOn( void );
    void off( void );
    void stageOff( void );
    char* getLabel( void );
    void writeDisplay( void );

  private:
    Adafruit_LEDBackpack* matrix;
    char*    label;
    uint8_t  cathode;
    uint16_t onMask;
    uint16_t offMask;
};

#endif
