const int Xpin = 34;
const int Ypin = 35;

#define BUTTON 15
#define BUTTON2 16
#define BUTTON3 17



int currentState;
int currentState2;
int currentState3;

// variable for storing the potentiometer value
int X = 0;
int Y = 0;


String STATE;

void setup() {
  Serial.begin(115200);
  delay(100);
  Serial.println("Start");
  delay(100);
  pinMode(BUTTON, INPUT_PULLUP);
  pinMode(BUTTON2, INPUT_PULLUP);
  pinMode(BUTTON3, INPUT_PULLUP);
}

void loop() {
  currentState = digitalRead(BUTTON);
  currentState2 = digitalRead(BUTTON2);
  currentState3 = digitalRead(BUTTON3);
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

  X = analogRead(Xpin);
  Y = analogRead(Ypin);

  Serial.println(String(X)+"  "+String(Y)+STATE);
  delay(30);
}