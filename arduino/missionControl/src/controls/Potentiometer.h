#ifndef _POTENTIOMETER_H
#define _POTENTIOMETER_H

class Potentiometer {
  public:
    Potentiometer( char* _potId, uint8_t _analogPin );
    void scan( void );
    char* id( void );
    uint8_t reading( void );
    bool hasChanged( void );

  private:
    uint8_t pin;
    char* potId;
    uint8_t currentState;
    uint8_t previousState;
};

#endif
