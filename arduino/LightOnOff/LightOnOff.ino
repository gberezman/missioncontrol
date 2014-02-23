int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  processSerial();
}

void processSerial(void) {
  if( Serial.available() ) {
    char charIn = Serial.read();
    if( charIn == '+' )
      ledOn();
    else
      ledOff();
  }
}

void ledOn() {
  digitalWrite(ledPin, HIGH);
}

void ledOff() {
  digitalWrite(ledPin, LOW);
}
