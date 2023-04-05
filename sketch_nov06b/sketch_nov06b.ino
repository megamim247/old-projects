int pin=A1  ;

void setup() {
pinMode(pin, INPUT);
Serial.begin(500000);
}


void loop() {
  // put your main code here, to run repeatedly:
int Value = analogRead(pin);
Serial.println(Value);
}
