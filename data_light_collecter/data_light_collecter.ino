#include <TimeLib.h>
#include <Ethernet.h>
#include <SPI.h>

int red = 2;
int yel = 3;
int gre = 4;
int lPin = A0;
int light = 0;

unsigned long lastPrintTime = 0;
//const unsigned long printInterval = 30000;
const unsigned long printInterval = 100;
 
void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  setTime(12,00,00,13,1,2025);
}

void loop() {
  light = analogRead(lPin);
  delay(1000);

  if(light > 35){
    digitalWrite(red, HIGH);
    digitalWrite(yel, LOW);
    digitalWrite(gre, LOW);
  }else if(light > 20){
    digitalWrite(red, LOW);
    digitalWrite(yel, HIGH);
    digitalWrite(gre, LOW);    
  }else{
    digitalWrite(red, LOW);
    digitalWrite(yel, LOW);
    digitalWrite(gre, HIGH);
  }
  
  if((millis() - lastPrintTime >= printInterval)) {
    Serial.println(light);
    lastPrintTime = millis();
  }
}
