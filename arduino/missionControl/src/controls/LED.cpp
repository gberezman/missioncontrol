#include <Wire.h>
#include "LED.h"

LED::LED(char* _label, Adafruit_LEDBackpack* _matrix, uint8_t _cathode, uint8_t _anode) {
    cathode = _cathode;
    matrix  = _matrix;
    label   = _label;
    onMask  = B1 << _anode; // e.g. 00000001000000000
    offMask = ~ (B1 << _anode); // e.g. 1111011111
}

char* LED::getLabel(void) {
    return label;
}

void LED::set( bool turnOn ) {
    if( turnOn )
        on();
    else
        off();
}

void LED::on(void) {
    stageOn();
    matrix->writeDisplay();
}

void LED::stageOn(void) {
    matrix->displaybuffer[cathode] |= onMask;
}

void LED::off(void) {
    stageOff();
    matrix->writeDisplay();
}

void LED::stageOff() {
    matrix->displaybuffer[cathode] &= offMask;
}

void LED::writeDisplay() {
    matrix->writeDisplay();
}
