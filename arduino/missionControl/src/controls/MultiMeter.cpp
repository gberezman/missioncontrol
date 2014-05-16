#include "MultiMeter.h"

void MultiMeter::setMeters( LEDMeter* _loMeter, LEDMeter* _hiMeter ) {
    loMeter = _loMeter;
    hiMeter = _hiMeter;
}

void MultiMeter::test( void ) {
    for( int i = 1; i < 25; i++ ) {
        if( i < 5 || i > 10 )
            setColor( i, BAR_LED_GREEN );
        else
            setColor( i, BAR_LED_RED );
    }

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

void MultiMeter::setColor( int8_t bar, int8_t color ) {
    if( bar < 13 )
        loMeter->setColor( bar, color );
    else
        hiMeter->setColor( bar - 12, color );
}
