#include "LEDNumber.h"
#include <string.h>

LEDNumber::LEDNumber( char* _label, LEDDigit _digits[] ) {
    label  = _label;
    digits = _digits;
}

char* LEDNumber::getLabel( void ) {
    return label;
}

void LEDNumber::set( char* value ) {
    for( int i = 0; i < 3; i++ ) {
        int digit = getDigit( value, i );
        digits[i].setDigit( digit );
    }
}

int LEDNumber::getDigit( char* value, int index ) {
    int shift = 3 - strlen( value );
    if( index < shift ) 
        return 0;

    return charToDigit( value[index - shift] );
}

int LEDNumber::charToDigit( char digitChar ) {
    int digit = digitChar - '0';

    if( digit < 0 || digit > 9 )
        digit = 0;

    return digit;
}

void LEDNumber::clear( void ) {
    for( int i = 0; i < 3; i++ )
        digits[i].clear();
}

