#include <Servo.h>
#include <ros.h>
#include <std_msgs/Int16.h>
Servo myservo;

void servoCb(const std_msgs::Int16& receivedMsg)
{
  int servo_angle = receivedMsg.data;
  if (servo_angle >= 0 && servo_angle <= 180)
  {
    myservo.write(servo_angle);
  }
}


ros::NodeHandle nh;
ros:: Subscriber<std_msgs::Int16> sub("servo_control", &servoCb);
// ros::Publisher<std_msgs::Int16> pub("", &);
void setup() {
  myservo.attach(9);
  nh.initNode();
  
  // nh.advertise(pub);
  
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  delay(10);
}
