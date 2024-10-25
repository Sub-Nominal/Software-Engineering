#include <Servo.h>
class ServoClass {
  private:
  Servo myservo;
  int pot;
  int servopin;
  int val;
  public:
  ServoClass(int servopin, int pot){
    this->servopin = servopin;
    this->pot = pot;
  }
  void Attach(){
  myservo.attach(servopin);
  }

  void move(){
  val = analogRead(pot);            
  val = map(val, 0, 1023, 0, 180);     
  myservo.write(val);                  
  delay(15);     
  }
};

ServoClass myservoA(9,0);
ServoClass myservoB(10,1);
ServoClass myservoC(11,2);

void setup(){
  myservoA.Attach();
  myservoB.Attach();
  myservoC.Attach();
  }
  void loop(){
    myservoA.move();
    myservoB.move();
    myservoC.move();
  }
