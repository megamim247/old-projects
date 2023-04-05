int pin=11  ;
int pin2=12  ;
int pin3=13 ;
void setup() {
pinMode(pin, INPUT);
pinMode(pin2, INPUT);
pinMode(pin3, INPUT);
Serial.begin(38400);
}


void loop() {
  // put your main code here, to run repeatedly:
int Value = digitalRead(pin);
int Value2 = digitalRead(pin2);
int Value3 = digitalRead(pin3);
Serial.println(Value);
Serial.println(Value2);
Serial.println(Value3);
Serial.println("b");
}
