/*
  NetPulse ESP32 firmware starter.
  Hardware and Wi-Fi logic will be added in stages.
  Do not commit real Wi-Fi credentials to this file.
*/
#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  delay(300);
  Serial.println();
  Serial.println("NetPulse booting...");
  Serial.println("Starter firmware: hardware checks pending.");
}

void loop() {
  // Phase 1 will add Wi-Fi connection, reachability and OLED output.
  delay(1000);
}
