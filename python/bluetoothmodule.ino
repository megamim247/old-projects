   int ledPin= 13;
   int light= 12;
   int bulb= 11;
   int fan= 10;
   int button1 = 0; 
   int button2 = 0;
      int button3 = 0;
         int button4 = 0;    
    int state = 0;
 int R1 = 0;
 int R2 = 0;
 int R3 = 0;
 int R4 = 0;
 
    void setup() {
      pinMode(ledPin, OUTPUT);
      digitalWrite(ledPin, LOW);
      pinMode(light, OUTPUT);
      digitalWrite(light, LOW);
       pinMode(bulb, OUTPUT);
      digitalWrite(bulb, LOW);
       pinMode(fan, OUTPUT);
      digitalWrite(fan, LOW);
     pinMode(button1, INPUT_PULLUP);
     pinMode(button2, INPUT_PULLUP);
     pinMode(button3, INPUT_PULLUP);
     pinMode(button4, INPUT_PULLUP);

      Serial.begin(9600); // Default communication rate of the Bluetooth module
    }
    void loop() {
      if(Serial.available() > 0){ // Checks whether data is comming from the serial port
        state = Serial.read(); // Reads the data from the serial port
     Serial.println(state);
     
     }
     
     if (state == 1) {
      
      digitalWrite(ledPin, HIGH); // Turn LED OFF
      //R1=1;
     }
     else if (state == 10) {
      digitalWrite(ledPin, LOW);
     //R1=0;
     } 
    else if (state == 2) {
      digitalWrite(light, HIGH);
     //R2=1;
     } 
    else if (state == 20) {
      digitalWrite(light, LOW);
     //R2=0;
     } 
         else if (state == 3) {
      digitalWrite(bulb, HIGH);
     //R3=1;
     } 
    else if (state == 30) {
      digitalWrite(bulb, LOW);
     //R3=0;
     } 
         else if (state == 4) {
      digitalWrite(fan, HIGH);
     //R4=1;
     } 
    else if (state == 40) {
      digitalWrite(fan, LOW);
     //R4=0;
     } 
    
      
  if(digitalRead(button1)==LOW){
      delay(200);
      R1++;
      if(R1==1){
        while(digitalRead(button1)==LOW){}
              digitalWrite(ledPin, LOW); 
        }
         if(R1==2){
          while(digitalRead(button1)==LOW){}
            R1=0;
              digitalWrite(ledPin, HIGH); 
        }}

   
  if(digitalRead(button2)==LOW){
      delay(200);
      R2++;
      if(R2==1){
        while(digitalRead(button2)==LOW){}
              digitalWrite(bulb, LOW); 
        }
         if(R2==2){
          while(digitalRead(button2)==LOW){}
            R2=0;
              digitalWrite(bulb, HIGH); 
        }}

           
  if(digitalRead(button3)==LOW){
      delay(200);
      R3++;
      if(R3==1){
        while(digitalRead(button3)==LOW){}
              digitalWrite(light, LOW); 
        }
         if(R3==2){
          while(digitalRead(button3)==LOW){}
            R3=0;
              digitalWrite(light, HIGH); 
        }}

           
  if(digitalRead(button4)==LOW){
      delay(200);
      R4++;
      if(R4==1){
        while(digitalRead(button4)==LOW){}
              digitalWrite(fan, LOW); 
        }
         if(R4==2){
          while(digitalRead(button4)==LOW){}
            R4=0;
              digitalWrite(fan, HIGH); 
        }}
    }
