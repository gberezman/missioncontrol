const int LED_EXTERNAL = 22;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LED_EXTERNAL, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  processSerial();
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

