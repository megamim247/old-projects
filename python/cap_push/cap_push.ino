int sensorPin=7; 
 int led = 13; 
 int buz = 12; 
void setup() {
  pinMode(led, OUTPUT);  
  pinMode(sensorPin, INPUT);
   pinMode(buz, OUTPUT);
  }
 
void loop() {
  int senseValue = digitalRead(sensorPin);
    if (senseValue == HIGH){
      
    digitalWrite(led, LOW); 
    digitalWrite(buz, HIGH); 
  }
  else{
    digitalWrite(led,HIGH);
    digitalWrite(buz,LOW);
  } 
  delay(50);
}
