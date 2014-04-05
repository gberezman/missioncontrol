#ifndef POTENTIOMETERS_H
#define POTENTIOMETERS_H

#include "Potentiometer.h"

class Potentiometers {
  public:
    void scan( void );
    void sendPotStates( void );
};

#endif
