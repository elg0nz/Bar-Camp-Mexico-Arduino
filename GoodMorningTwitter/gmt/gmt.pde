//connect the photoresistor on pin 0 
// Following the schematic on http://wiring.org.co/learning/examples/photoresistor.html

int ledPin = 13;                // choose the pin for the LED
int inputPin = 2;               // choose the input pin (for a pushbutton)
int val = 0;                    // variable for reading the pin status
int serInput =0;
int bPress = false;

void setup()
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);      // declare LED as output
  pinMode(inputPin, INPUT);     // declare pushbutton as input
}

void loop()
{
  val = digitalRead(inputPin);  // read input value
  if (val >= HIGH) {            // check if the input is HIGH
    bPress = true;
  }
  
  if(bPress){
      Serial.println('n');
      delay(100);
      bPress = false;
  }
  
  if (Serial.available() > 0) 
    serInput = Serial.read();     
  if(serInput == 'H')
      digitalWrite(ledPin, HIGH); // turn LED ON
  else  
      digitalWrite(ledPin, LOW);  // turn LED OFF
  Serial.println(analogRead(0));
  delay(100);
}

