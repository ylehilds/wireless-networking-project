#include <driver/dac.h>

void setup() {
  // put your setup code here, to run once:
  pinMode(23, OUTPUT);
  dac_output_enable(DAC_CHANNEL_1);
}

void loop() {
  // put your main code here, to run repeatedly:
// for (int i = 0; i < 255; i++) {
  dac_output_voltage(DAC_CHANNEL_1, 100);
  delay(1);
  dac_output_voltage(DAC_CHANNEL_1, 0);
  delay(1);
// }
} 
