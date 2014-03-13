#ifndef _LEDMETER_H
#define _LEDMETER_H

#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
#include "Adafruit_MCP23017.h"

class LEDMeter {
  public:
    LEDMeter(Adafruit_LEDBackpack* matrix, uint8_t baseCathode, uint8_t baseAnode);
    void clear(void);
    void setBars(uint8_t bars);

  private:
    Adafruit_LEDBackpack* matrix;
    uint8_t baseCathode;
    uint8_t baseAnode;
};

#endif
