#include "MultiMeter.h"

void MultiMeter::setMeters( LEDMeter* _loMeter, LEDMeter* _hiMeter ) {
    loMeter = _loMeter;
    hiMeter = _hiMeter;
}

void MultiMeter::test( void ) {
    for( int i = 1; i < 25; i++ ) {
        enableRange( i, i + 3 );
        delay( 50 );
    }
}

void MultiMeter::clear( void ) {
    loMeter->clear();
    hiMeter->clear();
}

void MultiMeter::enableRange( int8_t lo, int8_t hi ) {
    clear();
    
    for( int i = max( 1, lo ); i < min( hi, 25 ); i++ ) {
        if( i < 13 )
            loMeter->enableBar( i );
        else
            hiMeter->enableBar( i - 12 );
    }
}
