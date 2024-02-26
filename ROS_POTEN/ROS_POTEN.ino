#include <ros.h>
#include <std_msgs/Float32.h>

unsigned long previousMillis = 0;
const unsigned long interval = 1000; // 1 วินาที

ros::NodeHandle  nh;
std_msgs::Float32 sensordata;
std_msgs::Float32 sensordata1;
ros::Publisher pub ("Topic_Sensor", &sensordata );
ros::Publisher pub1 ("Topic_Sensor1", &sensordata1 );
float RPercent1 = 0.0;
float RPercent2 = 0.0;

void setup() 
{
  Serial.begin(115200);
  nh.initNode();
  nh.advertise(pub);
  nh.advertise(pub1);
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    float RValue1 = analogRead(A0); 
    float RValue2 = analogRead(A3); 
    
    RPercent1 = (static_cast<float>(RValue1) / 1023) * 100.0;
    RPercent2 = (static_cast<float>(RValue2) / 1023) * 100.0;

    sensordata.data = RPercent1;
    sensordata1.data = RPercent2;

    pub.publish(&sensordata);
    pub1.publish(&sensordata1);
    nh.spinOnce();

    Serial.print("R1 Percent: ");
    Serial.println(RPercent1);
    Serial.print("R2 Percent: ");
    Serial.println(RPercent2);
  
  }
}
