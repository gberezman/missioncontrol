#ifndef POTENTIOMETER_GEOMETRY_H
#define POTENTIOMETER_GEOMETRY_H

#include "../controls/Potentiometer.h"

class PotentiometerCollection {
    public:
        void scan( void );
        void sendPotStates( void );
        Potentiometer* getPot( char* label );

    private:
        static Potentiometer pots[];
};

#endif
