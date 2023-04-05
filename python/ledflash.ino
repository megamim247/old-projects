int led=13; // led is connected at pin # 13
int led2=12;
int led3=11;

void setup() {
pinMode(led,OUTPUT);
pinMode(led2,OUTPUT);
pinMode(led3,OUTPUT);
}

void loop() {
  digitalWrite(led,HIGH); //for turning on the led
  delay(1000);
   digitalWrite(led2,HIGH); //for turning on the led
  delay(1000);
   digitalWrite(led3,HIGH); //for turning on the led
  delay(1000);
  digitalWrite(led,LOW); // for turning off led 
  delay(1000);
  digitalWrite(led2,LOW); // for turning off led 
  delay(1000);
  digitalWrite(led3,LOW); // for turning off led 
  delay(1000);
}
