#define CH1 3
#define CH2 5
#define CH3 6
#define CH4 9
#define CH5 10

// Read the number of a given channel and convert to the range provided.
// If the channel is off, return the default value
int readChannel(int channelInput, int minLimit, int maxLimit, int defaultValue){
  int ch = pulseIn(channelInput, HIGH, 30000);
  if (ch < 100) return defaultValue;
  return map(ch, 1000, 2000, minLimit, maxLimit);
}

void setup(){
  Serial.begin(115200);
  pinMode(CH1, INPUT);
  pinMode(CH2, INPUT);
  pinMode(CH3, INPUT);
  pinMode(CH4, INPUT);
  pinMode(CH5, INPUT);
}

int ch1Value, ch2Value;

void loop() {
  ch1Value = readChannel(CH1, -100, 100, 0);
  ch2Value = readChannel(CH2, -100, 100, 0);
  if ((ch1Value<3 and ch1Value>-3) or ch1Value>100 or ch1Value<-100){
    ch1Value=0;
    }
   if ((ch2Value<3 and ch2Value>-3) or ch2Value>100 or ch2Value<-100){
    ch2Value=0;
    }
    if (ch1Value>95){
      ch1Value=100;
      }
    if (ch2Value>95){
      ch2Value=100;
      }
  
  Serial.print("Ch1: ");
  Serial.print(ch1Value);
  Serial.print(" Ch2: ");
  Serial.println(ch2Value);
}
