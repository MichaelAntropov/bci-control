#include <SoftwareSerial.h>

SoftwareSerial hc06(2, 3);

int E1 = 5;
int M1 = 4;
int E2 = 6;
int M2 = 7;

String cmd = "";

void setup() {
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
  Serial.begin(9600);
  hc06.begin(9600);
}

void loop() {
  while (hc06.available()) {
    cmd += (char)hc06.read();
    break;
  }

  if (cmd != "") {
        Serial.print("Command: ");
        Serial.println(cmd);

    // FORWARD
    if (cmd.compareTo("1") == 0) {
      Serial.println("FORWARD");
      digitalWrite(M1, LOW);
      analogWrite(E1, 255);
      digitalWrite(M2, LOW);
      analogWrite(E2, 255);
    }

    // BACK
    if (cmd.compareTo("2") == 0) {
      Serial.println("BACK");
      digitalWrite(M1, HIGH);
      analogWrite(E1, 255);
      digitalWrite(M2, HIGH);
      analogWrite(E2, 255);
    }

    // LEFT
    if (cmd.compareTo("3") == 0) {
      Serial.println("LEFT");
      digitalWrite(M1, LOW);
      analogWrite(E1, 255);
      digitalWrite(M2, HIGH);
      analogWrite(E2, 255);
    }

    // RIGHT
    if (cmd.compareTo("4") == 0) {
      Serial.println("RIGHT");
      digitalWrite(M1, HIGH);
      analogWrite(E1, 255);
      digitalWrite(M2, LOW);
      analogWrite(E2, 255);
    }

    delay(100);
    digitalWrite(M1, LOW);
    analogWrite(E1, 0);
    digitalWrite(M2, LOW);
    analogWrite(E2, 0);

    cmd = ""; //reset cmd
  }
}
