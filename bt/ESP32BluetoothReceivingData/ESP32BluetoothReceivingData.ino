<<<<<<< HEAD
//This example code is in the Public Domain (or CC0 licensed, at your option.)
//By Evandro Copercini - 2018
//
//This example creates a bridge between Serial and Classical Bluetooth (SPP)
//and also demonstrate that SerialBT have the same functionalities of a normal Serial

#include "BluetoothSerial.h"
#include <driver/dac.h>

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
  dac_output_enable(DAC_CHANNEL_1);

}

int count = 0; 
bool requested = false;
void loop() {
//  if (Serial.available()) {
//    Serial.println("inside Serial.available()");
//    SerialBT.write(Serial.read());
//  }
  if (SerialBT.available()) {
    requested = true;
    byte tempByte = SerialBT.read();
    // writes data to Serial arduino
//    Serial.print(count++);
//    Serial.print(" ");
//    Serial.println(tempByte);
    // writes data back to BT serial which python script is listening to
//    SerialBT.write(tempByte);

    dac_output_voltage(DAC_CHANNEL_1, tempByte);
    delayMicroseconds(90);
  }
  else if (requested) {
    SerialBT.write('k');
    requested = false;
  }
//  delay(20);
}
=======
//This example code is in the Public Domain (or CC0 licensed, at your option.)
//By Evandro Copercini - 2018
//
//This example creates a bridge between Serial and Classical Bluetooth (SPP)
//and also demonstrate that SerialBT have the same functionalities of a normal Serial

#include "BluetoothSerial.h"
#include <driver/dac.h>

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#define DELAY 50

BluetoothSerial SerialBT;
int playPause = 22; 
int next = 23;
int prev = 21;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
  dac_output_enable(DAC_CHANNEL_1);
//  pinMode(playPause, INPUT);
//  pinMode(next, INPUT);
//  pinMode(prev, INPUT);

}

int count = 0; 
bool requested = false;
void loop() {
  if (SerialBT.available()) {
    requested = true;
    byte tempByte = SerialBT.read();
    count++; 
    dac_output_voltage(DAC_CHANNEL_1, tempByte);
    delayMicroseconds(85);
    if (count == 256) {
      SerialBT.write('k');
      count = 0;
    }
  }
  checkButtons();
//  int pp = digitalRead(playPause);
//  Serial.println(pp);
//  if (pp) {
//    SerialBT.write('p');
//  }
}

int ppState = 0;
int prState = 0;
int nState = 0;
unsigned long ppDebounce = 0;
unsigned long prDebounce = 0;
unsigned long nDebounce = 0;
int ppReading = 0;
int prReading = 0;
int nReading = 0;

bool ppMsgSent = false;
bool prMsgSent = false;
bool nMsgSent = false;

void checkButtons() {
  ppReading = digitalRead(playPause);
  if (ppReading != ppState){
    ppDebounce = millis();
    ppMsgSent = false;
  }
  if (millis() - ppDebounce > DELAY) {
    if (!ppMsgSent && ppState == HIGH) {
      SerialBT.write('p');
      ppMsgSent = true;
    }
  }
  ppState = ppReading;

    prReading = digitalRead(prev);
  if (prReading != prState){
    prDebounce = millis();
    prMsgSent = false;
  }
  if (millis() - prDebounce > DELAY) {
    if (!prMsgSent && prState == HIGH) {
      SerialBT.write('q');
      prMsgSent = true;
    }
  }
  prState = prReading;

    nReading = digitalRead(next);
  if (nReading != nState){
    nDebounce = millis();
    nMsgSent = false;
  }
  if (millis() - nDebounce > DELAY) {
    if (!nMsgSent && nState == HIGH) {
      SerialBT.write('n');
      nMsgSent = true;
    }
  }
  nState = nReading;
}
>>>>>>> test_branch
