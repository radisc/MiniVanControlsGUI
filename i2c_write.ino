#include <Wire.h>
#include <Arduino.h>

int flag_int_received_from_PI = 0;
char data_to_send_PI[] = "hello PI";
String data_recieved_from_pi = "";
int state = 0;

void setup()
{               
  for(int i = 0; i < 56; i++){
    pinMode(i, OUTPUT);
    digitalWrite(i, HIGH);
  }
 
  ///temp to read various angles 
  Wire.begin(0x20);
  Wire.onReceive(receiveData);

  
  Serial.begin(57600);
}

void loop(){}

void receiveData(int byteCount) {

    while(Wire.available()) {
        flag_int_received_from_PI = Wire.read();
        state = Wire.read();
        if (state == 1)
          digitalWrite(flag_int_received_from_PI, HIGH);
        if (state == 0)
          digitalWrite(flag_int_received_from_PI, LOW);
        

        Serial.print("Data Received From PI:");
        Serial.println(flag_int_received_from_PI, DEC);
        Serial.println(state);
        
    }
}
