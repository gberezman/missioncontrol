#include "Expanders.h"

Expanders::Expanders( SwitchExpander _expanders[] ) {
    expanders = _expanders;
}

void Expanders::initialize( void ) {
    for( int i = 0; i < sizeof(expanders)/sizeof(SwitchExpander); i++ )
        expanders[i].initialize();
}

void Expanders::scan( void ){
    for( int i = 0; i < sizeof(expanders)/sizeof(SwitchExpander); i++ )
        expanders[i].scanSwitches();
}

void Expanders::sendSwitchStates( void ){
    for( int i = 0; i < sizeof(expanders)/sizeof(SwitchExpander); i++ )
        expanders[i].sendChangedStatesToSerial();
}

