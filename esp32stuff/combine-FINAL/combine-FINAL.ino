/*
  ESP32 Web Server - STA Mode
  modified on 25 MAy 2019
  by Mohammadreza Akbari @ Electropeak
  Home
*/
#include <LiquidCrystal_I2C.h>
#include <WiFi.h>
#include <WebServer.h>


#define BUTTON 17
#define BUTTON2 16
#define BUTTON3 4


int currentState;
int lastState = HIGH;
int currentState2;
int lastState2 = HIGH;
int currentState3;
int lastState3 = HIGH;


LiquidCrystal_I2C lcd(0x27,16,2); 

String UserInput = "";
String HTML = "<!DOCTYPE html>\
<html>\
<body>\
<h1>My First Web Server with ESP32 - Station Mode &#128522;</h1>\
</body>\
</html>";

// SSID & Password
const char* ssid = "Mansoor";  // Enter your SSID here
const char* password = "0508917346";  //Enter your Password here

WebServer server(80);  // Object of WebServer(HTTP port, 80 is defult)

void setup() {
  pinMode(BUTTON, INPUT_PULLUP);
  pinMode(BUTTON2, INPUT_PULLUP);
  pinMode(BUTTON3, INPUT_PULLUP);

  Serial.begin(115200);
  Serial.println("Try Connecting to ");
  Serial.println(ssid);

  lcd.init();
  lcd.clear();  
  lcd.setCursor(0,0);

  // Connect to your wi-fi modem
  WiFi.begin(ssid, password);

  // Check wi-fi is connected to wi-fi network
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected successfully");
  Serial.print("Got IP: ");
  Serial.println(WiFi.localIP());  //Show ESP32 IP on serial

  server.on("/", handle_root);

  server.begin();
  Serial.println("HTTP server started");
  delay(100); 
}

void loop() {
  server.handleClient();
  lastState = currentState;
  lastState2 = currentState2;
  lastState3 = currentState3;
  currentState = digitalRead(BUTTON);
  currentState2 = digitalRead(BUTTON2);
  currentState3 = digitalRead(BUTTON3);
  if(lastState == LOW && currentState == HIGH)
    handle_button();
  if(lastState2 == LOW && currentState2 == HIGH)
    handle_button2();
  if(lastState3 == LOW && currentState3 == HIGH)
    handle_button3();
    
}

// Handle root url (/)
void handle_root() {
  Serial.println("GIVE");
  delay(200);
  String UserInput1=Serial.readStringUntil('\n');
  String UserInput2=Serial.readStringUntil('\n');
  String UserInput3=Serial.readStringUntil('\n');
  String UserInput4=Serial.readStringUntil('\n');
  if (UserInput1==""){
    UserInput1=="Offline";
  }
  server.send(200, "text/html", "<!DOCTYPE html><html><body>"+UserInput1+" "+UserInput2+" "+UserInput3+" "+UserInput4+"</body></html>");
}
//Handle LCD
void handle_button() {
  Serial.println("GIVE");
  delay(100);
  lcd.backlight();
  String UserInput1=Serial.readStringUntil('\n');
  String UserInput2=Serial.readStringUntil('\n');
  String UserInput3=Serial.readStringUntil('\n');
  String UserInput4=Serial.readStringUntil('\n');
  if (UserInput1==""){
    UserInput1=="Offline";
  }
  lcd.setCursor(0,0);
  lcd.print(UserInput1);
  lcd.setCursor(0,1);
  lcd.print(UserInput2);
  lcd.setCursor(0,2);
  lcd.print(UserInput3);
  lcd.setCursor(0,3);
  lcd.print(UserInput4);
  delay(8000);
  lcd.noBacklight();
  lcd.clear();
}
void handle_button2() {
  Serial.println("GIVE2");
  delay(100);
  lcd.backlight();
  String UserInput1=Serial.readStringUntil('\n');
  String UserInput2=Serial.readStringUntil('\n');
  String UserInput3=Serial.readStringUntil('\n');
  String UserInput4=Serial.readStringUntil('\n');
  if (UserInput1=="\n"){
    UserInput1=="Offline";
  }
  lcd.setCursor(0,0);
  lcd.print(UserInput1);
  lcd.setCursor(0,1);
  lcd.print(UserInput2);
  lcd.setCursor(0,2);
  lcd.print(UserInput3);
  lcd.setCursor(0,3);
  lcd.print(UserInput4);
  delay(8000);
  lcd.noBacklight();
  lcd.clear();
}
void handle_button3() {
  Serial.println("GIVE3");
  delay(100);
  lcd.backlight();
  String UserInput1=Serial.readStringUntil('\n');
  String UserInput2=Serial.readStringUntil('\n');
  String UserInput3=Serial.readStringUntil('\n');
  String UserInput4=Serial.readStringUntil('\n');
  if (UserInput1=="\n"){
    UserInput1=="Offline";
  }
  lcd.setCursor(0,0);
  lcd.print(UserInput1);
  lcd.setCursor(0,1);
  lcd.print(UserInput2);
  lcd.setCursor(0,2);
  lcd.print(UserInput3);
  lcd.setCursor(0,3);
  lcd.print(UserInput4);
  delay(8000);
  lcd.noBacklight();
  lcd.clear();
}

