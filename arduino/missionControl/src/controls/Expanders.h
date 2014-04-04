#ifndef _EXPANDERS_H
#define _EXPANDERS_H

#include "SwitchExpander.h"

class Expanders {
  public:
    Expanders( SwitchExpander expanders[] );
    void initialize( void );
    void scan( void );
    void sendSwitchStates( void );

  private:
    SwitchExpander* expanders;
};

#endif
