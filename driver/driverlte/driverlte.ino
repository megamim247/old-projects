int readChannel(int channelInput){
  int ch = pulseIn(channelInput, HIGH, 24000);
  return (ch-1490)/5;
}

void setup(){
  Serial.begin(500000);
  pinMode(3, INPUT);
  pinMode(5, INPUT);
  pinMode(6, INPUT);
}
int ch1,ch2,ch3;
void loop() {
  ch1=readChannel(3);
  ch2=readChannel(5);
  ch3=readChannel(6);
  Serial.print(ch1);
  Serial.print(" ");
  Serial.print(ch2);
  Serial.print(" ");
  Serial.println(ch3);
}
