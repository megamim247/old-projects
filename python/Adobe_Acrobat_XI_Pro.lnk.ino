//Mic on off led
int led=13; // led pin and sound pin are not changed throughout the process
int buzz=12;
int soundpin=A5;
int threshold=200; // sets threshold for sound sensor
int i=0;
void setup() {
  Serial.begin(9600);
pinMode(led,OUTPUT);
pinMode(buzz,OUTPUT);
pinMode(soundpin,INPUT);
}
void loop() {
  
  int soundsens=analogRead(soundpin); // read analog data from sensor
Serial.println(soundsens);
  if (soundsens>=threshold) {
    if(i==0){
    digitalWrite(led, HIGH); // turn led on
    digitalWrite(buzz, HIGH); 
i=1;
    delay(200);
  }
  else if(i==1){
    digitalWrite(led, LOW);
     digitalWrite(buzz, LOW);
  i=0;
delay(200);  
  }}
}
