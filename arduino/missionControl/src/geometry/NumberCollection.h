#ifndef NUMBER_COLLECTION_H
#define NUMBER_COLLECTION_H

#include "../controls/LEDNumber.h"

class NumberCollection {

    public:
        LEDNumber* getNumber( char* label );
        void testAll( void );
        void clearAll( void );

    private:
        static LED IHR0[];
        static LED IHR1[];
        static LED IHR2[];
        static LEDDigit IHR[];

        static LED AHR0[];
        static LED AHR1[];
        static LED AHR2[];
        static LEDDigit AHR[];

        static LED ABR0[];
        static LED ABR1[];
        static LED ABR2[];
        static LEDDigit ABR[];

        static LED Pitch0[];
        static LED Pitch1[];
        static LED Pitch2[];
        static LEDDigit Pitch[];

        static LED Yaw0[];
        static LED Yaw1[];
        static LED Yaw2[];
        static LEDDigit Yaw[];

        static LED Roll0[];
        static LED Roll1[];
        static LED Roll2[];
        static LEDDigit Roll[];

        static LEDNumber numbers[];
};

#endif

