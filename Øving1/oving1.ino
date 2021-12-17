#include "ProcessShield.h"

ProcessShield ps = ProcessShield();

void setup() {
  Serial.begin(9600);
  ps.set_U6_channel_resistance(3, 10000);
  

}

//void loop() {
//  if (ps.get_button_SW1() == HIGH){
//    ps.set_LED_D1(HIGH);
//    ps.set_LED_D2(HIGH);
//    ps.set_LED_D3(HIGH);
//  } else {
//    ps.set_LED_D1(LOW);
//    ps.set_LED_D2(LOW);
//    ps.set_LED_D3(LOW);
//  }
//}

//void loop() {
//    ps.set_LED_D1(HIGH);
//    ps.set_LED_D2(HIGH);
//    ps.set_LED_D3(HIGH);
//    delay(500);
//    ps.set_LED_D1(LOW);
//    ps.set_LED_D2(LOW);
//    ps.set_LED_D3(LOW);
//    delay(500);
//}

void loop(){
  Serial.println(ps.get_potmeter_RV1_voltage());
  Serial.print(",");
  ps.set_DAC_U4_voltage(ps.get_potmeter_RV1_voltage());
  Serial.println(ps.get_output_A1_voltage());
}
