#include "ExpanderLED.h"

ExpanderLED::ExpanderLED(char* _label, Adafruit_MCP23017* _mcp, int _pin, bool _doInvert) {
    label    = _label;
    mcp      = _mcp;
    pin      = _pin;
    doInvert = _doInvert;
}

void ExpanderLED::initialize( void ) {
  mcp->pinMode( pin, OUTPUT );
  set( false );
}

char* ExpanderLED::getLabel(void) {
    return label;
}

void ExpanderLED::set( bool turnOn ) {
    bool enable = doInvert ? ! turnOn : turnOn;
    if( enable )
        high();
    else
        low();
}

void ExpanderLED::high(void) {
    mcp->digitalWrite( pin, HIGH );
}

void ExpanderLED::low(void) {
    mcp->digitalWrite( pin, LOW );
}
