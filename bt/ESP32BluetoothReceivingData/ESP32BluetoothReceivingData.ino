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
