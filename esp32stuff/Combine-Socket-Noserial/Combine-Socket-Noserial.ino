#include <LiquidCrystal_I2C.h>
#include <WiFi.h>
#include <SPI.h>

#define BUTTON 17
#define BUTTON2 16
#define BUTTON3 4
int currentState;
int lastState = HIGH;
int currentState2;
int lastState2 = HIGH;
int currentState3;
int lastState3 = HIGH;

const char* url = "mim-server-1.ddnsfree.com";
bool connected = "true";

LiquidCrystal_I2C lcd(0x27,16,2); 

String data = "";
String dataarray[4]={"","","",""};
int count;

// SSID & Password
const char* ssid = "Mansoor";  // Enter your SSID here
const char* password = "0508917346";  //Enter your Password here

WiFiServer wifiServer(3000);

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

  wifiServer.begin();
  
}

void loop() {
  WiFiClient client = wifiServer.available();
  if(client.connected()){
    Serial.println("client connected");
  }
  while (client.connected()){
    connected=true;
    lastState = currentState;
    lastState2 = currentState2;
    lastState3 = currentState3;
    currentState = digitalRead(BUTTON);
    currentState2 = digitalRead(BUTTON2);
    currentState3 = digitalRead(BUTTON3);
    data = "";
    if(lastState == LOW && currentState == HIGH){
      client.println("1");
      delay(100);
      data="";
      while (client.available() > 0){
        data+= (char) client.read();;
      };
    }
    if(lastState2 == LOW && currentState2 == HIGH){
      client.println("2");
      delay(100);
      data="";
      while (client.available() > 0){
        data+= (char) client.read();
      };
    }
    if(lastState3 == LOW && currentState3 == HIGH){
      client.println("3");
      delay(100);
      data="";
      while (client.available() > 0){
        data+= (char) client.read();
      };
    }
    if (data!=""){
      count=0;
      dataarray[1]="";
      dataarray[2]="";
      dataarray[3]="";
      dataarray[0]=data;
      while(data.length()>20 && count<4) {
        dataarray[count]=data.substring(0,20);
        data=data.substring(20,data.length());
        count++;
      }
      if (count<3){
        dataarray[count]=data;
      }
      lcd.backlight();
      lcd.setCursor(0,0);
      lcd.print(dataarray[0]);
      lcd.setCursor(0,1);
      lcd.print(dataarray[1]);
      lcd.setCursor(20,0);
      lcd.print(dataarray[2]);
      lcd.setCursor(20,1);
      lcd.print(dataarray[3]);
      delay(8000);
      lcd.noBacklight();
      lcd.clear();
    }
  }
  if (connected){
    connected=false;
    Serial.println("client disconnected");
    lcd.backlight();
    lcd.setCursor(0,0);
    lcd.print("DISCONNECTED");
    delay(8000);
    lcd.noBacklight();
    lcd.clear();
  }
  delay(8000);
}
