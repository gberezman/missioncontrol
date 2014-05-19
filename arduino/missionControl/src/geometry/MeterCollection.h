#ifndef LEDMETER_GEOMETRY_H
#define LEDMETER_GEOMETRY_H

#include "../controls/LEDMeter.h"

class MeterCollection {
    public:
        LEDMeter* getMeter( char* label );
        void testAll( void );
        void clearAll( void );

    private:
        static LEDMeter METERS[];
};

#endif
