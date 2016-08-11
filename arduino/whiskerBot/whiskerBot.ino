#include <Servo.h>
Servo servoLeft;
Servo servoRight;

void moveForward(){
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
}
void moveBackward(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
}
void turnLeft(){
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1300);
  delay(rand()%250+250);
}
void turnRight(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
  delay(rand()%250+250);
}

void setup() {
  // put your setup code here, to run once:
  // 7 is right whisker
  // 5 is left whisker
  // 4 is turn indicator LED
  servoLeft.attach(13);
  servoRight.attach(12);
  pinMode(4, OUTPUT);
  pinMode(5, INPUT);
  pinMode(7, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(4,LOW);
  if(digitalRead(5) == LOW){ //left whisker
    digitalWrite(4,HIGH);
    moveForward();
    delay(200);
    turnRight();
    digitalWrite(4,LOW);
    
  }
  else if (digitalRead(7) == LOW){ //right whisker
    digitalWrite(4,HIGH);
    moveForward();
    delay(200);
    turnLeft();
    digitalWrite(4,LOW);
  }
  else{
    moveBackward();
  }
}
