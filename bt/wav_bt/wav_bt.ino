
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
int output = 0;
int currloop = 0;
void setup() {
  Serial.begin(9600);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
  dac_output_enable(DAC_CHANNEL_1);
}

void loop() {
  // put your main code here, to run repeatedly:
//   if (Serial.available()) {
//     output = Serial.read();
//   }
  if (SerialBT.available()) {
      output = SerialBT.read();
      Serial.print(currloop);
      Serial.print(" ");
      Serial.println(output);
    dac_output_voltage(DAC_CHANNEL_1, output);
    delayMicroseconds(90);
    currloop++;
  }
}
