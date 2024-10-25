

#include <Servo.h>

Servo base;
Servo shoulder;
Servo arm;  // create Servo object to control a servo


int posb = 0; 
int poss = 0;
int posa = 0;   // variable to store the servo position

void setup() {
  base.attach(9); 
  shoulder.attach(10);
  arm.attach(11); // attaches the servo on pin 9 to the Servo object
}

void loop() {
  for (posb = 90; posb <= 180; posb += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    base.write(posb);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
  for (posb = 180; posb >= 90; posb -= 1) { // goes from 180 degrees to 0 degrees
    base.write(posb);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }

  for (posa = 0; posa <= 180; posa += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    arm.write(posa);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
  for (posa = 180; posa >= 0; posa -= 1) { // goes from 180 degrees to 0 degrees
    arm.write(posa);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
  
  for (poss = 0; poss <= 90; poss += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    shoulder.write(poss);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
  for (poss = 90; poss >= 0; poss-= 1) { // goes from 180 degrees to 0 degrees
    shoulder.write(poss);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15 ms for the servo to reach the position
  }
}



