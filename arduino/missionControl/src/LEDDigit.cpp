#include <Wire.h>
#include "LEDDigit.h"

LEDDigit::LEDDigit(char* _label, Adafruit_LEDBackpack* _matrix, uint8_t _cathode, uint8_t _baseAnode) {
    cathode   = _cathode;
    baseAnode = _baseAnode;
    matrix    = _matrix;
    label     = _label;
}

char* LEDDigit::getLabel(void) {
    return label;
}

void LEDDigit::setDigit(uint8_t value) {
}

void LEDDigit::clear(void) {
}
