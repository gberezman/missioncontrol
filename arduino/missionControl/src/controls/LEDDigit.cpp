#include "LEDDigit.h"
#include <Arduino.h>"

LEDDigit::LEDDigit(char* _label, LED _ledArray[8]) {
    label    = _label;
    ledArray = _ledArray;
}

char* LEDDigit::getLabel(void) {
    return label;
}

void LEDDigit::setDigit(uint8_t value) {
    for( int segment = 0; segment < 8; segment++ ) {
        if( numbers[value][segment] ) 
            ledArray[segment].on();
        else 
            ledArray[segment].off();
    }
}

void LEDDigit::clear(void) {
    for( int i = 0; i < 8; i++ )
        ledArray[i].off();
}
