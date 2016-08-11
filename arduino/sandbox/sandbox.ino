void setup() {
  // put your setup code here, to run once:
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  pinMode(4, HIGH);
  delay(250);
  pinMode(4, LOW);
  delay(250);
  for (int i = 0; i <2; i++){
      pinMode(5, HIGH);
      delay(250);
      pinMode(5, LOW);
      delay(250);
  }
}
