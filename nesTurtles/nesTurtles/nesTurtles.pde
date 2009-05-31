#include <NESpad.h>
NESpad nintendo = NESpad();

byte state = 0;

void setup() {
  Serial.begin(115200);  
}

void loop() {
  
  state = nintendo.buttons();

  if (state & NES_A)  Serial.print('a');
  if (state & NES_B)  Serial.print('b');
  if (state & NES_UP)  Serial.print('u');
  if (state & NES_DOWN)  Serial.print('d');
  if (state & NES_LEFT)  Serial.print('l');
  if (state & NES_RIGHT)  Serial.print('r');
  if (state & NES_START)  Serial.print('s');
  //Serial.println(~state, BIN);
  delay(250);
}
