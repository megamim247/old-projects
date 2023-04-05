int led = 13; 
int buz = 12; // the pin that the LED is atteched to
int sensor = 7;              // the pin that the sensor is atteched to
int val = 0;                 // variable to store the sensor status (value)

void setup() {
  pinMode(led, OUTPUT);      // initalize LED as an output
  pinMode(buz, OUTPUT);
  pinMode(sensor, INPUT);    // initialize sensor as an input
}

void loop(){
  val = digitalRead(sensor);   // read sensor value
  if (val == HIGH) {           // check if the sensor is HIGH
    digitalWrite(led, HIGH);   // turn LED ON
    digitalWrite(buz, HIGH);
    delay(200);                // delay 100 milliseconds 
  } 
  else {
      digitalWrite(led, LOW); // turn LED OFF
      digitalWrite(buz, LOW);
      delay(200);             // delay 200 milliseconds 
  }
}
