#ifndef EXPANDERLED_DEFINITIONS_H
#define EXPANDERLED_DEFINITIONS_H

#include "../controls/ExpanderLED.h"

class ExpanderLEDCollection {
  public:
    ExpanderLED* getLed( char* label );
    void initialize( void );
    void enableAll( void );
    void disableAll( void );

  private:
    static ExpanderLED expanderLeds[];
};

#endif
