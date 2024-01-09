#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def run(val):
	if val.data == "Hello world":
		rospy.loginfo("Hello world too")
	else:
		rospy.loginfo(val.data)
		
		
		
if __name__ == "__main__":
	sub = rospy.Subscriber("chatter",String,callback=run)
	rospy.init_node("Listenser")
	rospy.spin()

