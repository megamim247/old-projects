const int Xpin = 34;
const int Ypin = 35;
const int XRpin = 33;
const int YRpin = 32;

#define BUTTON 15
#define BUTTON2 16
#define BUTTON3 17
//keypad
#define bottomkey1 5
#define bottomkey2 23
#define bottomkey3 18
#define bottomkey4 19
#define bottomkey5 21
#define bottomkey6 22
#define topkey1 12
#define topkey2 13
#define topkey3 14
#define topkey4 25
#define topkey5 26
#define topkey6 27



int currentState;
int currentState2;
int currentState3;

int bottomCurrentState1;
int bottomCurrentState2;
int bottomCurrentState3;
int bottomCurrentState4;
int bottomCurrentState5;
int bottomCurrentState6;

int topCurrentState1;
int topCurrentState2;
int topCurrentState3;
int topCurrentState4;
int topCurrentState5;
int topCurrentState6;

// variable for storing the potentiometer value
int X = 0;
int Y = 0;

int XR = 0;
int YR = 0;


String STATE;

void setup() {
  Serial.begin(115200);
  delay(100);
  Serial.println("Start");
  delay(100);
  pinMode(BUTTON, INPUT_PULLUP);
  pinMode(BUTTON2, INPUT_PULLUP);
  pinMode(BUTTON3, INPUT_PULLUP);
  pinMode(bottomkey1, INPUT_PULLUP);
  pinMode(bottomkey2, INPUT_PULLUP);
  pinMode(bottomkey3, INPUT_PULLUP);
  pinMode(bottomkey4, INPUT_PULLUP);
  pinMode(bottomkey5, INPUT_PULLUP);
  pinMode(bottomkey6, INPUT_PULLUP);
  pinMode(topkey1, INPUT_PULLUP);
  pinMode(topkey2, INPUT_PULLUP);
  pinMode(topkey3, INPUT_PULLUP);
  pinMode(topkey4, INPUT_PULLUP);
  pinMode(topkey5, INPUT_PULLUP);
  pinMode(topkey6, INPUT_PULLUP);
}

void loop() {
  currentState = digitalRead(BUTTON);
  currentState2 = digitalRead(BUTTON2);
  currentState3 = digitalRead(BUTTON3);
  bottomCurrentState1 = digitalRead(bottomkey1);
  bottomCurrentState2 = digitalRead(bottomkey2);
  bottomCurrentState3 = digitalRead(bottomkey3);
  bottomCurrentState4 = digitalRead(bottomkey4);
  bottomCurrentState5 = digitalRead(bottomkey5);
  bottomCurrentState6 = digitalRead(bottomkey6);
  topCurrentState1 = digitalRead(topkey1);
  topCurrentState2 = digitalRead(topkey2);
  topCurrentState3 = digitalRead(topkey3);
  topCurrentState4 = digitalRead(topkey4);
  topCurrentState5 = digitalRead(topkey5);
  topCurrentState6 = digitalRead(topkey6);
  STATE="";
  if (currentState == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
  if (currentState2 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
  if (currentState3 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
  


  if (bottomCurrentState1 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
    if (bottomCurrentState2 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
    if (bottomCurrentState3 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
    if (bottomCurrentState4 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
    if (bottomCurrentState5 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
    if (bottomCurrentState6 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };



  if (topCurrentState1 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
    if (topCurrentState2 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
    if (topCurrentState3 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
    if (topCurrentState4 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
    if (topCurrentState5 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
    if (topCurrentState6 == HIGH) {
    STATE+=" 1";
  } else {
    STATE+=" 0";
  };
  X = analogRead(Xpin);
  Y = analogRead(Ypin);
  
  XR = analogRead(XRpin);
  YR = analogRead(YRpin);
  Serial.println(String(X)+" "+String(Y)+STATE+" "+String(XR)+" "+String(YR));
  delay(100);
}