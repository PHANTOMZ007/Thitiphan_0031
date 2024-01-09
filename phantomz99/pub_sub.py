#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
def run(pose):
	if pose.x > 10.0 or pose.x < 1.0 or pose.y >10.0 or pose.y <1.0:
		cmd = Twist()
		cmd.linear.x = 0.5
		cmd.linear.y = 0.5
		cmd.linear.z = 0.5
		cmd.angular.x = 0.5
		cmd.angular.y = 0.5
		cmd.angular.z = 0.5
		pub.publish(cmd)
	else:
		cmd = Twist()
		cmd.linear.x = 0.5
		cmd.linear.y = 0.5
		cmd.linear.z = 0.5
		cmd.angular.x = 0.5
		cmd.angular.y = 0.5
		cmd.angular.z = 0.5
		pub.publish(cmd)
if __name__ == "__main__":
	rospy.init_node("control")
	pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
	sub = rospy.Subscriber("/turtle1/pose",Pose,callback=run)
	rospy.spin()
