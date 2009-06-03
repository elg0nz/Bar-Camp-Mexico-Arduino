//Midiservos by Gonzalo Maldonado
//Moves a servo each time it recives a midi note

//Uses Mididuino libraries http://ruinwesen.com/mididuino
//Servo Connections http://www.arduino.cc/playground/ComponentLib/Servo
//Yellow: Data In (connect to the port you want to use for servo communications
//Red: +5V
//Black: GND

//Midi Connection: check http://ruinwesen.com/support-files/mididuino/mididuino-documentation.pdf
#include <MidiUart.h> 
#include <Midi.h> 
#define ledPin 13

MidiClass Midi; 
Servo myservo; //must create one Servo instance for each servomotor

void onNoteOnCallback(byte *msg) { 
  digitalWrite(ledPin, HIGH); 
  myservo.write(180);              // tell servo move 90 degrees

} 
void onNoteOffCallback(byte *msg) { 
  digitalWrite(ledPin, LOW); 
  myservo.write(90);              // tell servo to move 180 degrees
} 

void setup() { 
  MidiUart.init();
  Midi.setOnNoteOnCallback(onNoteOnCallback);
  Midi.setOnNoteOffCallback(onNoteOffCallback); 
  pinMode(ledPin, OUTPUT);  
  myservo.attach(9);  // attaches the servo on pin 9 to the servo
} 

void loop() { 
  while (MidiUart.avail()) { 
    Midi.handleByte(MidiUart.getc()); 
  }
} 
