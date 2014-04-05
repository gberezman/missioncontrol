#include "Expanders.h"
#include "SwitchExpander.h"
#include "../geometry/ExpanderGeometry.h"

void Expanders::initialize( void ) {
    for( int i = 0; i < sizeof(SWITCH_EXPANDERS)/sizeof(SwitchExpander); i++ )
        SWITCH_EXPANDERS[i].initialize();
}

void Expanders::scan( void ){
    for( int i = 0; i < sizeof(SWITCH_EXPANDERS)/sizeof(SwitchExpander); i++ )
        SWITCH_EXPANDERS[i].scanSwitches();
}

void Expanders::sendSwitchStates( void ){
    for( int i = 0; i < sizeof(SWITCH_EXPANDERS)/sizeof(SwitchExpander); i++ )
        SWITCH_EXPANDERS[i].sendChangedStatesToSerial();
}

