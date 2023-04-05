#include <LedControl.h>
int DIN_PIN = 10;
int CS_PIN = 9;
int CLK_PIN = 8;
int button=6;
int k=0;
//***************************************//
//-------------Paste Code Here------------//
//***************************************//

const uint64_t IMAGES[] = {
  0xffff18181b1e1c18,
  0x00384492aa827c00,
  0x3f1f0f1b3160c080,
  0xff8199a581a581ff,
  0xff81bda5a5bd81ff,
  0xc3663c18386cc6c3,
  0xff8199a581a581ff,
  0xff81a59981a581ff,
  0x0103070f1f3f7fff,
  0xfffefcf8f0e0c080,
  0xffffc3c3c3c3ffff
};
int IMAGES_LEN = sizeof(IMAGES)/8;
LedControl display = LedControl(DIN_PIN, CLK_PIN, CS_PIN);

//***************************************//
//------------------END------------------//
//***************************************//

void setup() {
  pinMode(button,INPUT_PULLUP);
  display.clearDisplay(0);
  display.shutdown(0, false);
  display.setIntensity(0, 8);
}

void displayImage(uint64_t image) {
  for (int i = 0; i < 8; i++) {
    byte row = (image >> i * 8) & 0xFF;
    for (int j = 0; j < 8; j++) {
      display.setLed(0, i, j, bitRead(row, j));
    }
  }
}

int i = 0;

void loop() {

  if(digitalRead(button)==LOW ){
   while(digitalRead(button)==LOW){}; 
    
  displayImage(IMAGES[i]);
    delay(300);
  i++;
  }
  
  if (i >= IMAGES_LEN ) {
    i = 0;
  }
}
