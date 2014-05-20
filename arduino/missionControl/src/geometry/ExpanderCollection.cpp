#include "ExpanderCollection.h"

#include "Expanders.h"

extern SwitchExpander SWITCH_EXPANDERS[];

void ExpanderCollection::initialize( void ) {
    for( int i = 0; i < sizeof(SWITCH_EXPANDERS)/sizeof(SwitchExpander); i++ )
        SWITCH_EXPANDERS[i].initialize();
}

void ExpanderCollection::scan( void ){
    for( int i = 0; i < sizeof(SWITCH_EXPANDERS)/sizeof(SwitchExpander); i++ )
        SWITCH_EXPANDERS[i].scanSwitches();
}

void ExpanderCollection::sendSwitchStates( void ){
    for( int i = 0; i < sizeof(SWITCH_EXPANDERS)/sizeof(SwitchExpander); i++ )
        SWITCH_EXPANDERS[i].sendChangedStatesToSerial();
}

SwitchExpander* ExpanderCollection::getExpander( int address ) {
    return &SWITCH_EXPANDERS[address];
}
