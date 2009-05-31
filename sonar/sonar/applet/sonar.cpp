#include "WProgram.h"
void setup();
void loop();
*// Sonar by Gonzalo Maldonado

// Includes code by others such as:
// Sweep by BARRAGAN <http://barraganstudio.com> 
// http://www.tigoe.net/pcomp/code/category/arduinowiring/17
//Uses devantech srf04 sonar http://www.robot-electronics.co.uk/htm/srf04tech.htm
#include <Servo.h> 
#define echoPin 2             // the SRF04's echo pin
#define initPin 3             // the SRF04's init pin
unsigned long pulseTime = 0;  // variable for reading the pulse
 
Servo myservo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 

void setup() 
{ 
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
   // make the init pin an output:
  pinMode(initPin, OUTPUT);
  // make the echo pin an input:
  pinMode(echoPin, INPUT);
  // initialize the serial port:
  Serial.begin(115200);
} 
 
 
void loop() 
{ 
  for(pos = 0; pos < 180; pos += 1)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 1 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    digitalWrite(initPin, HIGH);
    delay(15);                       // waits 15ms for the servo to reach the position 
    digitalWrite(initPin, LOW);
    pulseTime = pulseIn(echoPin, HIGH);
    Serial.println(pulseTime, DEC);
  } 
  for(pos = 180; pos>=1; pos-=1)     // goes from 180 degrees to 0 degrees 
  {                                
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    digitalWrite(initPin, HIGH);
    delay(15);                       // waits 15ms for the servo to reach the position 
    digitalWrite(initPin, LOW);
    pulseTime = pulseIn(echoPin, HIGH);
    Serial.println(pulseTime, DEC); 
  } 
} 

int main(void)
{
	init();

	setup();
    
	for (;;)
		loop();
        
	return 0;
}

