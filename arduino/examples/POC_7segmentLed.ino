const int LED_EXTERNAL = 22;
const int SWITCH = 52;

int switchState;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LED_EXTERNAL, OUTPUT);
  
  // Enable segment LED pins and digit pins for output
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
  pinMode(A4, OUTPUT);
  pinMode(A5, OUTPUT);
  pinMode(A6, OUTPUT);
  pinMode(A7, OUTPUT);
  pinMode(A8, OUTPUT);
  pinMode(A9, OUTPUT);
  pinMode(A10, OUTPUT);
  pinMode(A11, OUTPUT);
  pinMode(A12, OUTPUT);
  
  switchState = digitalRead(SWITCH);
  
  Serial.begin(115200);
}

void loop() {
  processSerial();
  processSwitch();
  processLed();
  delay(20);
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

void processLed(void) {
  digitalWrite(A10, HIGH);
  digitalWrite(A1, LOW);
  digitalWrite(A2, LOW);
  digitalWrite(A3, LOW);
  digitalWrite(A4, LOW);
  digitalWrite(A5, LOW);
  digitalWrite(A6, LOW);
  digitalWrite(A7, LOW);
  digitalWrite(A8, LOW);
}

