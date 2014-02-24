const int LED_EXTERNAL = 22;
const int SWITCH = 52;

boolean wasSwitchOpen;

int switchState;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LED_EXTERNAL, OUTPUT);
  
  switchState = digitalRead(SWITCH);
  
  Serial.begin(115200);
}

void loop() {
  processSerial();
  processSwitch();
}

void processSerial(void) {
  if( Serial.available() ) {
    char charIn = Serial.read();
    if( charIn == '+' )
      ledOn(LED_BUILTIN);
    else if( charIn == '-' )
      ledOff(LED_BUILTIN);
    else if( charIn == 'x' )
      ledOn(LED_EXTERNAL);
    else if( charIn == 'o' )
      ledOff(LED_EXTERNAL);
  }
}

void ledOn(int pin) {
  digitalWrite(pin, HIGH);
}

void ledOff(int pin) {
  digitalWrite(pin, LOW);
}

void processSwitch(void) {
  int newState = digitalRead(SWITCH);
  if( switchState != newState ) {
    switchState = newState;
    if( newState == LOW )
      Serial.write('o');
    else
      Serial.write('x');
  }
}
