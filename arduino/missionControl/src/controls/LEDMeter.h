#ifndef _LEDMETER_H
#define _LEDMETER_H

#include "Adafruit_LEDBackpack.h"

#define BAR_LED_GREEN  B11110000
#define BAR_LED_RED    B00001111
#define BAR_LED_YELLOW B11111111

static uint16_t ALL_YELLOW[] = {
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW
};

static uint16_t ALL_RED[] = {
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_RED
};

static uint16_t ALL_GREEN[] = {
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN
};

static uint16_t TWELVE_BAR_MIDRANGE_COLORS[] = {
  BAR_LED_RED,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_RED
};

static uint16_t TWELVE_BAR_QTY_COLORS[] = {
  BAR_LED_RED,
  BAR_LED_RED,
  BAR_LED_YELLOW,
  BAR_LED_YELLOW,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN,
  BAR_LED_GREEN
};

class LEDMeter {
  public:
    LEDMeter(char* label, Adafruit_LEDBackpack* matrix, uint8_t baseCathode, uint8_t baseAnode, uint16_t* colors);
    void clear(void);
    void setBars(uint8_t bars);
    char* getLabel( void );
    void enableBar(uint8_t bar);

  private:
    void setDisplayBuffer( uint8_t pin, uint8_t value, uint8_t color );
    uint16_t applyNewAnodes(uint16_t current, uint8_t value);
    uint8_t getColor( uint8_t bars );
    Adafruit_LEDBackpack* matrix;
    char* label;
    uint8_t  baseCathode;
    uint8_t  baseAnode;
    uint16_t* colors;
    uint16_t anodeMask;
    uint8_t bars;
};

#endif
