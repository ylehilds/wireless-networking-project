
#include <driver/dac.h>

int output = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  
  dac_output_enable(DAC_CHANNEL_1);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
//   Serial.println("I got something!!");
//    Serial.println(Serial.readString());
    output = Serial.read();
//    Serial.println(output);
    dac_output_voltage(DAC_CHANNEL_1, output);
    delayMicroseconds(90);
  }
}
