//Initialize Motor 1
int motor1Pin1 = 7;
int motor1Pin2 = 6;
int enable1Pin = 9;
 
//Initialize Motor 2
int motor2Pin1 = 5; 
int motor2Pin2 = 4; 
int enable2Pin = 3;

int HeadLight = 12;
int BackLight = 13;


int state;
void setup() {
    // sets the pins as outputs:
    
    pinMode(motor1Pin1, OUTPUT);
    pinMode(motor1Pin2, OUTPUT);
    pinMode(enable1Pin, OUTPUT);
    pinMode(motor2Pin1, OUTPUT);
    pinMode(motor2Pin2, OUTPUT);
    pinMode(enable2Pin, OUTPUT);
    pinMode(HeadLight,OUTPUT);
    pinMode(BackLight,OUTPUT);
     
      digitalWrite(HeadLight,LOW);
      digitalWrite(BackLight,LOW);
        
    
   
    // initialize serial communication at 9600 bits per second:
    Serial.begin(9600);
}
 
void loop() {
    //if some date is sent, reads it and saves in state
    if(Serial.available())
    {     
      state = Serial.read();
    }
   // delay(50);
    // if the state is '1' the DC motor will go forward 
     
      if (state == 1) // forward
    {        
      digitalWrite(motor1Pin1, LOW); 
      digitalWrite(motor1Pin2, HIGH);
      digitalWrite(motor2Pin1, LOW);
      digitalWrite(motor2Pin2, HIGH);
      analogWrite(enable1Pin, 255);
      analogWrite(enable2Pin, 255);
    //  Serial.println("Forward");
    }
   
    else if (state == 2)  // left
    {
      //turn left
        digitalWrite(motor1Pin1, HIGH); 
        digitalWrite(motor1Pin2, LOW); 
        digitalWrite(motor2Pin1, LOW);
        digitalWrite(motor2Pin2, HIGH);
        analogWrite(enable1Pin, 255);
        analogWrite(enable2Pin, 255);
      //  Serial.println("left");
    }
     
    else if (state == 3) // right
    {
      //TURN RIGHT
         digitalWrite(motor1Pin1, LOW); 
      digitalWrite(motor1Pin2, HIGH);
      digitalWrite(motor2Pin1, HIGH);
      digitalWrite(motor2Pin2, LOW);
        analogWrite(enable1Pin, 255);
        analogWrite(enable2Pin, 255);
        //Serial.println("right");
      
    }
    
    else if (state == 4) //reverse
    {
        
         digitalWrite(motor1Pin1, HIGH); 
      digitalWrite(motor1Pin2, LOW);
      digitalWrite(motor2Pin1, HIGH);
      digitalWrite(motor2Pin2, LOW);
        analogWrite(enable1Pin, 255);
        analogWrite(enable2Pin, 255);       
        //Serial.println("reverse");
    }
    else if (state == 5) //  Stop
    {
        digitalWrite(enable1Pin, 0);
        digitalWrite(enable2Pin, 0);
        delay(300);
        //Serial.println("stop");
    }
      if (state == 10) // Nos
    { 
      digitalWrite(motor1Pin1, LOW); 
      digitalWrite(motor1Pin2, HIGH);
      digitalWrite(motor2Pin1, LOW);
      digitalWrite(motor2Pin2, HIGH);
      analogWrite(enable1Pin, 255);
      analogWrite(enable2Pin, 255);
      //Serial.println("NOS");
    }
    else if (state==6)
    {
      digitalWrite(HeadLight,HIGH);
    //  Serial.println("Front Light On");
    }
    else if (state==7)
    {
      digitalWrite(BackLight,HIGH); 
      //Serial.println("Back Light On");
    }
    else if (state==60)
    {
      digitalWrite(HeadLight,LOW);
      //Serial.println("Front Light Off");
    }
    else if (state==70)
    {
      digitalWrite(BackLight,LOW);   
      //Serial.println("Back Light Off");
    }
delay(100);
}
