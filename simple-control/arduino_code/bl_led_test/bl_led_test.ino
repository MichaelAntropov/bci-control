#include <SoftwareSerial.h>

SoftwareSerial hc06(2, 3);

#define LED_PIN 13

String cmd = "";

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);
  Serial.begin(9600);
  hc06.begin(9600);
}

void loop() {
  while (hc06.available() > 0) {
    cmd += (char)hc06.read();
  }

  if (cmd != "") {
    Serial.print("Command: ");
    Serial.println(cmd);

    if (cmd.compareTo("1") == 0) {
      digitalWrite(LED_PIN, HIGH);
    }

    if (cmd.compareTo("0") == 0) {
      digitalWrite(LED_PIN, LOW);
    }

    cmd = ""; //reset cmd
  }
}
