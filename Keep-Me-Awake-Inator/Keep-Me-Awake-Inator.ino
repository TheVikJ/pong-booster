#include <Servo.h>

Servo myservo;
int incomingByte;

void setup()
{
  myservo.attach(9);
  Serial.begin(9600);
}

void loop() 
{
  if (Serial.available() > 0) 
  {
    incomingByte = Serial.read();
    
    if (incomingByte == 'F') 
    {
      myservo.write(180);
      delay(1000);
      myservo.write(90);
    }
  }
}
