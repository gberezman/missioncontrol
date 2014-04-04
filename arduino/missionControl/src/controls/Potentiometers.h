#ifndef POTENTIOMETERS_H
#define POTENTIOMETERS_H

#include "Potentiometer.h"

class Potentiometers {
  public:
    Potentiometers( Potentiometer pots[] );
    void scan( void );
    void sendPotStates( void );

  private:
    Potentiometer* pots;
};

#endif
