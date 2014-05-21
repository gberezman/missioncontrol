#include "ExpanderLEDCollection.h"

#include "../controls/SwitchExpander.h"

extern SwitchExpander SWITCH_EXPANDERS[]; 

ExpanderLED ExpanderLEDCollection::expanderLeds[] = {
    ExpanderLED( "ArmAbort", SWITCH_EXPANDERS[2].getMCP(), 1, true ),
    ExpanderLED( "MasterAlarm", SWITCH_EXPANDERS[2].getMCP(), 8, false )
};

void ExpanderLEDCollection::initialize( void ) {
    for( int ledIndex = 0; ledIndex < sizeof( expanderLeds ) / sizeof( ExpanderLED ); ledIndex++ )
        expanderLeds[ledIndex].initialize();
}

ExpanderLED* ExpanderLEDCollection::getLed( char* label ) {
    for( int ledIndex = 0; ledIndex < sizeof( expanderLeds ) / sizeof( ExpanderLED ); ledIndex++ ) {
        if( strcmp( label, expanderLeds[ledIndex].getLabel() ) == 0 ) {
            return &expanderLeds[ledIndex];
        }
    }

    return NULL;
}

void ExpanderLEDCollection::enableAll( void ) {
    for( int ledIndex = 0; ledIndex < sizeof( expanderLeds ) / sizeof( ExpanderLED ); ledIndex++ ) {
        expanderLeds[ledIndex].set( true );
    }
}

void ExpanderLEDCollection::disableAll( void ) {
    for( int ledIndex = 0; ledIndex < sizeof( expanderLeds ) / sizeof( ExpanderLED ); ledIndex++ ) {
        expanderLeds[ledIndex].set( false );
    }
}
