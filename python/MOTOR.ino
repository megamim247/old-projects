int button= 7; 
 int motor = 11;
 int led = 13;
   
void setup() {
  pinMode(led, OUTPUT);  
  pinMode(motor, OUTPUT);  
  pinMode(button, INPUT_PULLUP);
 
  }
 
void loop() {
  int buttonstate = digitalRead(button);
   
    if (buttonstate == LOW){
    digitalWrite(led, HIGH);
     digitalWrite(motor, HIGH);   
  }
  else{
    digitalWrite(led,LOW);
    digitalWrite(motor,LOW);
  } 
  delay(50);
}
