#include "NumberCollection.h"

extern Adafruit_LEDBackpack matrixA;
extern Adafruit_LEDBackpack matrixB;
extern Adafruit_LEDBackpack matrixC;
extern Adafruit_LEDBackpack matrixD;
extern Adafruit_LEDBackpack matrixE;

LED NumberCollection::IHR0[] = {
    LED( "top right",    &matrixB, 6, 6 ),
    LED( "bottom right", &matrixB, 2, 6 ),
    LED( "bottom",       &matrixB, 4, 6 ),
    LED( "bottom left",  &matrixB, 7, 6 ),
    LED( "top left",     &matrixB, 0, 6 ),
    LED( "top",          &matrixB, 5, 6 ),
    LED( "middle",       &matrixB, 1, 6 ),
    LED( "point",        &matrixB, 3, 6 )
};

LED NumberCollection::IHR1[] = {
    LED( "top right",    &matrixB, 6, 7 ),
    LED( "bottom right", &matrixB, 2, 7 ),
    LED( "bottom",       &matrixB, 4, 7 ),
    LED( "bottom left",  &matrixB, 7, 7 ),
    LED( "top left",     &matrixB, 0, 7 ),
    LED( "top",          &matrixB, 5, 7 ),
    LED( "middle",       &matrixB, 1, 7 ),
    LED( "point",        &matrixB, 3, 7 )
};

LED NumberCollection::IHR2[] = {
    LED( "top right",    &matrixB, 5, 8 ),
    LED( "bottom right", &matrixB, 2, 8 ),
    LED( "bottom",       &matrixB, 4, 8 ),
    LED( "bottom left",  &matrixB, 7, 8 ),
    LED( "top left",     &matrixB, 0, 8 ),
    LED( "top",          &matrixB, 6, 8 ),
    LED( "middle",       &matrixB, 1, 8 ),
    LED( "point",        &matrixB, 3, 8 )
};

LED NumberCollection::AHR0[] = {
    LED( "top right",    &matrixB, 5, 3 ),
    LED( "bottom right", &matrixB, 2, 3 ),
    LED( "bottom",       &matrixB, 4, 3 ),
    LED( "bottom left",  &matrixB, 7, 3 ),
    LED( "top left",     &matrixB, 0, 3 ),
    LED( "top",          &matrixB, 6, 3 ),
    LED( "middle",       &matrixB, 1, 3 ),
    LED( "point",        &matrixB, 3, 3 )
};

LED NumberCollection::AHR1[] = {
    LED( "top right",    &matrixB, 5, 4 ),
    LED( "bottom right", &matrixB, 2, 4 ),
    LED( "bottom",       &matrixB, 4, 4 ),
    LED( "bottom left",  &matrixB, 7, 4 ),
    LED( "top left",     &matrixB, 0, 4 ),
    LED( "top",          &matrixB, 6, 4 ),
    LED( "middle",       &matrixB, 1, 4 ),
    LED( "point",        &matrixB, 3, 4 )
};

LED NumberCollection::AHR2[] = {
    LED( "top right",    &matrixB, 5, 5 ),
    LED( "bottom right", &matrixB, 2, 5 ),
    LED( "bottom",       &matrixB, 4, 5 ),
    LED( "bottom left",  &matrixB, 7, 5 ),
    LED( "top left",     &matrixB, 0, 5 ),
    LED( "top",          &matrixB, 6, 5 ),
    LED( "middle",       &matrixB, 1, 5 ),
    LED( "point",        &matrixB, 3, 5 )
};

LED NumberCollection::ABR0[] = {
    LED( "top right",    &matrixB, 5, 0 ),
    LED( "bottom right", &matrixB, 2, 0 ),
    LED( "bottom",       &matrixB, 4, 0 ),
    LED( "bottom left",  &matrixB, 7, 0 ),
    LED( "top left",     &matrixB, 0, 0 ),
    LED( "top",          &matrixB, 6, 0 ),
    LED( "middle",       &matrixB, 1, 0 ),
    LED( "point",        &matrixB, 3, 0 )
};

LED NumberCollection::ABR1[] = {
    LED( "top right",    &matrixB, 5, 1 ),
    LED( "bottom right", &matrixB, 2, 1 ),
    LED( "bottom",       &matrixB, 4, 1 ),
    LED( "bottom left",  &matrixB, 7, 1 ),
    LED( "top left",     &matrixB, 0, 1 ),
    LED( "top",          &matrixB, 6, 1 ),
    LED( "middle",       &matrixB, 1, 1 ),
    LED( "point",        &matrixB, 3, 1 )
};

LED NumberCollection::ABR2[] = {
    LED( "top right",    &matrixB, 0, 2 ),
    LED( "bottom right", &matrixB, 2, 2 ),
    LED( "bottom",       &matrixB, 4, 2 ),
    LED( "bottom left",  &matrixB, 7, 2 ),
    LED( "top left",     &matrixB, 5, 2 ),
    LED( "top",          &matrixB, 6, 2 ),
    LED( "middle",       &matrixB, 1, 2 ),
    LED( "point",        &matrixB, 3, 2 )
};

LED NumberCollection::Pitch0[] = {
    LED( "top right",    &matrixA, 7, 6 ),
    LED( "bottom right", &matrixA, 3, 6 ),
    LED( "bottom",       &matrixA, 1, 6 ),
    LED( "bottom left",  &matrixA, 2, 6 ),
    LED( "top left",     &matrixA, 6, 6 ),
    LED( "top",          &matrixA, 5, 6 ),
    LED( "middle",       &matrixA, 0, 6 ),
    LED( "point",        &matrixA, 4, 6 )
};

LED NumberCollection::Pitch1[] = {
    LED( "top right",    &matrixA, 7, 7 ),
    LED( "bottom right", &matrixA, 3, 7 ),
    LED( "bottom",       &matrixA, 1, 7 ),
    LED( "bottom left",  &matrixA, 2, 7 ),
    LED( "top left",     &matrixA, 6, 7 ),
    LED( "top",          &matrixA, 5, 7 ),
    LED( "middle",       &matrixA, 0, 7 ),
    LED( "point",        &matrixA, 4, 7 )
};

LED NumberCollection::Pitch2[] = {
    LED( "top right",    &matrixA, 7, 8 ),
    LED( "bottom right", &matrixA, 3, 8 ),
    LED( "bottom",       &matrixA, 1, 8 ),
    LED( "bottom left",  &matrixA, 2, 8 ),
    LED( "top left",     &matrixA, 6, 8 ),
    LED( "top",          &matrixA, 5, 8 ),
    LED( "middle",       &matrixA, 0, 8 ),
    LED( "point",        &matrixA, 4, 8 )
};

LED NumberCollection::Yaw0[] = {
    LED( "top right",    &matrixA, 7, 10 ),
    LED( "bottom right", &matrixA, 3, 10 ),
    LED( "bottom",       &matrixA, 1, 10 ),
    LED( "bottom left",  &matrixA, 2, 10 ),
    LED( "top left",     &matrixA, 6, 10 ),
    LED( "top",          &matrixA, 5, 10 ),
    LED( "middle",       &matrixA, 0, 10 ),
    LED( "point",        &matrixA, 4, 10 )
};

LED NumberCollection::Yaw1[] = {
    LED( "top right",    &matrixA, 7, 11 ),
    LED( "bottom right", &matrixA, 3, 11 ),
    LED( "bottom",       &matrixA, 1, 11 ),
    LED( "bottom left",  &matrixA, 2, 11 ),
    LED( "top left",     &matrixA, 6, 11 ),
    LED( "top",          &matrixA, 5, 11 ),
    LED( "middle",       &matrixA, 0, 11 ),
    LED( "point",        &matrixA, 4, 11 )
};

LED NumberCollection::Yaw2[] = {
    LED( "top right",    &matrixA, 7, 12 ),
    LED( "bottom right", &matrixA, 3, 12 ),
    LED( "bottom",       &matrixA, 1, 12 ),
    LED( "bottom left",  &matrixA, 2, 12 ),
    LED( "top left",     &matrixA, 6, 12 ),
    LED( "top",          &matrixA, 5, 12 ),
    LED( "middle",       &matrixA, 0, 12 ),
    LED( "point",        &matrixA, 4, 12 )
};

LED NumberCollection::Roll0[] = {
    LED( "top right",    &matrixA, 7, 13 ),
    LED( "bottom right", &matrixA, 3, 13 ),
    LED( "bottom",       &matrixA, 1, 13 ),
    LED( "bottom left",  &matrixA, 2, 13 ),
    LED( "top left",     &matrixA, 6, 13 ),
    LED( "top",          &matrixA, 5, 13 ),
    LED( "middle",       &matrixA, 0, 13 ),
    LED( "point",        &matrixA, 4, 13 )
};

LED NumberCollection::Roll1[] = {
    LED( "top right",    &matrixA, 7, 14 ),
    LED( "bottom right", &matrixA, 3, 14 ),
    LED( "bottom",       &matrixA, 1, 14 ),
    LED( "bottom left",  &matrixA, 2, 14 ),
    LED( "top left",     &matrixA, 6, 14 ),
    LED( "top",          &matrixA, 5, 14 ),
    LED( "middle",       &matrixA, 0, 14 ),
    LED( "point",        &matrixA, 4, 14 )
};

LED NumberCollection::Roll2[] = {
    LED( "top right",    &matrixA, 7, 15 ),
    LED( "bottom right", &matrixA, 3, 15 ),
    LED( "bottom",       &matrixA, 1, 15 ),
    LED( "bottom left",  &matrixA, 2, 15 ),
    LED( "top left",     &matrixA, 6, 15 ),
    LED( "top",          &matrixA, 5, 15 ),
    LED( "middle",       &matrixA, 0, 15 ),
    LED( "point",        &matrixA, 4, 15 )
};

LEDDigit NumberCollection::IHR[] = {
  LEDDigit( "IHR0", IHR0 ),
  LEDDigit( "IHR1", IHR1 ),
  LEDDigit( "IHR2", IHR2 )
};

LEDDigit NumberCollection::AHR[] = {
  LEDDigit( "AHR0", AHR0 ),
  LEDDigit( "AHR1", AHR1 ),
  LEDDigit( "AHR2", AHR2 )
};

LEDDigit NumberCollection::ABR[] = {
  LEDDigit( "ABR0", ABR0 ),
  LEDDigit( "ABR1", ABR1 ),
  LEDDigit( "ABR2", ABR2 )
};

LEDDigit NumberCollection::Pitch[] = {
  LEDDigit( "Pitch0", Pitch0 ),
  LEDDigit( "Pitch1", Pitch1 ),
  LEDDigit( "Pitch2", Pitch2 )
};

LEDDigit NumberCollection::Yaw[] = {
  LEDDigit( "Yaw0", Yaw0 ),
  LEDDigit( "Yaw1", Yaw1 ),
  LEDDigit( "Yaw2", Yaw2 )
};

LEDDigit NumberCollection::Roll[] = {
  LEDDigit( "Roll0", Roll0 ),
  LEDDigit( "Roll1", Roll1 ),
  LEDDigit( "Roll2", Roll2 )
};

LEDNumber NumberCollection::numbers[] = {
  LEDNumber( "ABR", ABR ),
  LEDNumber( "AHR", AHR ),
  LEDNumber( "IHR", IHR ),
  LEDNumber( "Pitch", Pitch ),
  LEDNumber( "Yaw", Yaw ),
  LEDNumber( "Roll", Roll )
};

LEDNumber* NumberCollection::getNumber( char* label ) {
  for( int i = 0; i < sizeof( numbers ) / sizeof( LEDNumber ); i++ )
    if( strcmp( label, numbers[i].getLabel() ) == 0 )
        return &numbers[i];

  return NULL;
}

void NumberCollection::testAll( void ) {
    char buffer[4];
    for( int value = 0; value < 1000; value += 111 ) {
        itoa( value, buffer, 10 );
        for( int i = 0; i < sizeof( numbers ) / sizeof( LEDNumber ); i++ ) {
            numbers[i].set( buffer );
        }
        delay( 10 );
    }
}

void NumberCollection::clearAll( void ) {
  for( int i = 0; i < sizeof( numbers ) / sizeof( LEDNumber ); i++ )
        numbers[i].clear();
}
