#ifndef _POTENTIOMETER_H
#define _POTENTIOMETER_H

class Potentiometer {
  public:
    Potentiometer( uint8_t _potId, uint8_t _analogPin );
    void scan( void );
    uint8_t id( void );
    uint8_t reading( void );
    bool hasChanged( void );

  private:
    uint8_t pin;
    uint8_t potId;
    uint8_t currentState = 0;
    uint8_t previousState = 0;
};

#endif
