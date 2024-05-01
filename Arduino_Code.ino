#define RedLed 3 //Assign Led Pin
#define BUZZER_PIN 5 //Assign Buzzer Pin
#define Sensor A0 // Assign Sensor Pin
#include <Wire.h> 
#include <LiquidCrystal_I2C.h> //Include LCD Library
#include <pitches.h> //Include Melody Library
LiquidCrystal_I2C lcd(0x27,16,2); //LCD Format

// Melody Notes
int melody[] = {  
  NOTE_E5, NOTE_D5, NOTE_FS4, NOTE_GS4, 
  NOTE_CS5, NOTE_B4, NOTE_D4, NOTE_E4, 
  NOTE_B4, NOTE_A4, NOTE_CS4, NOTE_E4,
  NOTE_A4
  };

// Melody Duration
int durations[] = {
  8, 8, 4, 4,
  8, 8, 4, 4,
  8, 8, 4, 4,
  2
  };
void setup() {
  pinMode(RedLed, OUTPUT); //Red Led Pin Format
  pinMode(BUZZER_PIN, OUTPUT); //Buzzer Pin Format
  lcd.init(); //Start LCD
  }

void loop()  {
  int VoltageRead = analogRead(Sensor); //Read Sensor
  float Vo = (VoltageRead / 1023.0)*5; //Float var & Change
  float TempC = (Vo - 0.5 ) * 100.0; //Find Temp in Celsius
  float TempF = (1.8) * (TempC) + 32.0; //Change Celsius into Fahrenheit
 
  lcd.backlight(); //Turn on LCD
  lcd.clear(); //Clear LCD Screen
  lcd.setCursor(0,0); //Set Cursor to first row
  lcd.print("Tempeature F = "); //Printing
  lcd.setCursor(1,1); //Set Cursor to second row
  lcd.print(TempF); //Printing var TempF
  delay(500); // Delay by 0.5 sec

  if (TempF >95 || TempF < 85) {
      lcd.setCursor(0,0); //Set Cursor to first row
      lcd.clear(); //Clear LCD Screen
      lcd.print("    WARNING"); //Printing
      playNokia(); // Play Melody
      delay(1000); // Delay 1 sec
  } else {
    digitalWrite(RedLed, LOW); //If in range turn off Led
    digitalWrite(BUZZER_PIN, LOW); //Turn off Buzzer
  }
}

void playNokia() {
  int size = sizeof(durations) / sizeof(int);

  for (int note = 0; note < size; note++) {
    //to calculate the note duration, take one second divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int duration = 1000 / durations[note];
    digitalWrite(RedLed,HIGH);
    tone(BUZZER_PIN, melody[note], duration);
    delay(50);
    digitalWrite(RedLed,LOW);
    //to distinguish the notes, set a minimum time between them.
    //the note's duration
    int pauseBetweenNotes = duration *1.0;
    delay(pauseBetweenNotes);

    //stop the tone playing:
    noTone(BUZZER_PIN);
    }
}