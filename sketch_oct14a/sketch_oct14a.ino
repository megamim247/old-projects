#include <PPMReader.h>

// Initialize a PPMReader on digital pin 3 with 6 expected channels.
byte interruptPin = 3;
byte channelAmount = 6;
PPMReader ppm(interruptPin, channelAmount);

void setup() {
    Serial.begin(9600);
}

void loop() {
    // Print latest valid values from all channels
    for (byte channel = 1; channel <= channelAmount; ++channel) {
        unsigned value = ppm.latestValidChannelValue(channel, 0);
        Serial.print(String(value) + "\t");
    }
    Serial.println();
    delay(20);
}
