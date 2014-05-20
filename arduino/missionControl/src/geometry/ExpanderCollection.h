#ifndef _EXPANDERCOLLECTION_H
#define _EXPANDERCOLLECTION_H

#include "../controls/SwitchExpander.h"

class ExpanderCollection {
      public:
        void initialize( void );
        void scan( void );
        void sendSwitchStates( void );
        SwitchExpander* getExpander( int address );
};

#endif
