//Motoru pieslēgšana ar H-Brige
#define IN1 8
#define IN2 7
#define IN3 5
#define IN4 4
#define echoPin 13 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 12 //attach pin D3 Arduino to pin Trig of HC-SR04

// LCD displeja lietas (es nesaprot)
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement


void setup()
{
 Serial.begin(9600);
 pinMode (IN1, OUTPUT);
 pinMode (IN2, OUTPUT);
 pinMode (IN3, OUTPUT);
 pinMode (IN4, OUTPUT);
 pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
 pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
 lcd.init();
 lcd.backlight();
 lcd.setCursor(0,0);
 lcd.print("Francis"); // print some text in Serial Monitor
 lcd.setCursor(0,1);
 lcd.print("Arduino");
 delay(5000);
 lcd.clear();

  
}


void atpakal () {
 digitalWrite (IN1, LOW);
 digitalWrite (IN2, HIGH);
 digitalWrite (IN3, LOW);
 digitalWrite (IN4, HIGH);
}
void uzPrieksu(){
digitalWrite (IN1, HIGH);
digitalWrite (IN2, LOW);
digitalWrite (IN3, LOW);
digitalWrite (IN4, HIGH);
}
void apstaties(){
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, LOW);
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, LOW);
}


void loop()
{
digitalWrite(trigPin, LOW);
  delayMicroseconds(50);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(100);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2 - 0.99; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  lcd.setCursor(0,0);
  lcd.print("Distance: ");
  lcd.setCursor(0,1);
  lcd.print(distance);
  if (distance > 40) {
    uzPrieksu();
  }
  else if (distance == 40){
      apstaties();
  }
  else if (distance < 38) {
    atpakal();
  }

}