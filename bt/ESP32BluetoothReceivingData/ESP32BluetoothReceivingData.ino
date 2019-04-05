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
//int next = 23;
//int prev = 21;

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
unsigned long ppDebounce = 0;
int ppReading = 0;
bool ppMsgSent = false;

void checkButtons() {
  ppReading = digitalRead(playPause);
  if (ppReading != ppState){
    ppDebounce = millis();
    ppMsgSent = false;
  }
//  Serial.print("ppState: ");
//  Serial.print(ppState);
//  Serial.print(" ppReading: ");
//  Serial.print(ppReading);
//  Serial.print(" time: ");
//  Serial.println(millis() - ppDebounce);
  if (millis() - ppDebounce > DELAY) {
    if (!ppMsgSent && ppState == HIGH) {
      SerialBT.write('p');
      ppMsgSent = true;
    }
  }
  ppState = ppReading;
}
