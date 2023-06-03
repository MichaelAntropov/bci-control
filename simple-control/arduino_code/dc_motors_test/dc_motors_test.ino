int E1 = 5;
int M1 = 4;
int E2 = 7;
int M2 = 6;

String action = "BACK";

void setup() {
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  if (action.compareTo("FORWARD") == 0) {
    digitalWrite(M1, LOW);
    analogWrite(E1, 255);
    digitalWrite(M2, LOW);
    analogWrite(E2, 255);
  }

  if (action.compareTo("BACK") == 0) {
    digitalWrite(M1, HIGH);
    analogWrite(E1, 255);
    digitalWrite(M2, HIGH);
    analogWrite(E2, 255);
  }

  if (action.compareTo("LEFT") == 0) {
    digitalWrite(M1, LOW);
    analogWrite(E1, 255);
    digitalWrite(M2, HIGH);
    analogWrite(E2, 255);
  }

  if (action.compareTo("RIGHT") == 0) {
    digitalWrite(M1, HIGH);
    analogWrite(E1, 255);
    digitalWrite(M2, LOW);
    analogWrite(E2, 255);
  }

  delay(1000);
  digitalWrite(M1, LOW);
  digitalWrite(M2, LOW);
  delay(4000);
}
