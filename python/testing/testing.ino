int MOTORA_R = 7;
int MOTORA_B=6;
int MOTORB_R=5;
int MOTORB_B=4;
int PWMA=9;
int PWMB=3;
void setup() {
pinMode(MOTORA_R, OUTPUT); 
pinMode(MOTORA_B, OUTPUT);
pinMode(MOTORB_R, OUTPUT); 
pinMode(MOTORB_B, OUTPUT); 
pinMode(PWMA, OUTPUT); 
pinMode(PWMB, OUTPUT); 
digitalWrite(PWMA, HIGH);
digitalWrite(PWMB, HIGH); 
} void loop() {  

//FORWARD
digitalWrite(MOTORA_R,  HIGH); 
digitalWrite(MOTORA_B, LOW); 
digitalWrite(MOTORB_R, LOW); 
digitalWrite(MOTORB_B, HIGH);  
} 
