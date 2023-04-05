#include <LedControl.h>
int DIN_PIN = 10;
int CS_PIN = 9;
int CLK_PIN = 8;
int timedelay = 500;
//***************************************//
//-------------Paste Code Here------------//
//***************************************//


const uint64_t IMAGES[] = {
  0x0000013e20203e01,
  0x0000013e20203e01,
  0x0000013e20203e01,
  0x0000013e20203e01,
  0x0000013e20203e01,
  0x0000013e20203e01,
  0x0000013e20203e01,
  0x0000013e20203e01,
  0x0000013e20203e01
};
const int IMAGES_LEN = sizeof(IMAGES)/8;




//***************************************//
//------------------END------------------//
//**************************************//


LedControl display = LedControl(DIN_PIN, CLK_PIN, CS_PIN);


void setup() {
  display.clearDisplay(0);
  display.shutdown(0, false);
  display.setIntensity(0, 10);
}


int i = 0;
void loop() {
  displayImage(IMAGES[i]);
  if (++i >= IMAGES_LEN ) {
    i = 0;
  }
  delay(timedelay);
}

void displayImage(uint64_t image) {
  for (int i = 0; i < 8; i++) {
    byte row = (image >> i * 8) & 0xFF;
    for (int j = 0; j < 8; j++) {
      display.setLed(0, i, j, bitRead(row, j));
    }
  }
}
