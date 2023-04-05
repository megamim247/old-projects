#define CH1 3
#define CH2 5
#define CH3 6
#define CH4 9
#define CH5 10

// Read the number of a given channel and convert to the range provided.
// If the channel is off, return the default value
int readChannel(int channelInput, int minLimit, int maxLimit){
  int ch = pulseIn(channelInput, HIGH, 30000);
  return map(ch, 1000, 2000, minLimit, maxLimit);
}

void setup(){
  Serial.begin(500000);
  pinMode(CH1, INPUT);
  pinMode(CH2, INPUT);
  pinMode(CH3, INPUT);
  pinMode(CH4, INPUT);
  pinMode(CH5, INPUT);
}
int ch1,ch2,ch3,ch4,ch5;
void loop() {
  ch1=readChannel(CH1, -100, 100);
  ch2=readChannel(CH2, -100, 100);
  ch3=readChannel(CH3, -100, 100);
  ch4=readChannel(CH4, -100, 100);
  ch5=readChannel(CH5, -100, 100);
  Serial.print(ch1);
  Serial.print(" ");
  Serial.print(ch2);
  Serial.print(" ");
  Serial.print(ch3);
  Serial.print(" ");
  Serial.print(" ");
  Serial.println(ch5);
}
