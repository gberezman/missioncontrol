#ifndef _EXPANDERCOLLECTION_H
#define _EXPANDERCOLLECTION_H

#include "../controls/SwitchExpander.h"

class ExpanderCollection {
      public:
        void initialize( void );
        void scan( void );
        void sendSwitchStates( void );

    private:
        static char* exp0Switches[16];
        static char* exp1Switches[16];
        static char* exp2Switches[16];
        static char* exp3Switches[16];
        static SwitchExpander SWITCH_EXPANDERS[4];
};

#endif
