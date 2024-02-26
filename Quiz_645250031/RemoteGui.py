#!/usr/bin/env python3
from tkinter import *
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from std_srvs.srv import SetBool

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x400")

rospy.init_node("Turtle_Control")
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)
pub_motion = rospy.Publisher("Motion", String, queue_size=10)

def fw():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z = 0.0
    pub.publish(cmd)
    pub_motion.publish("Fw")

def bw():
    cmd = Twist()
    cmd.linear.x = -LinearVel.get()
    cmd.angular.z = 0.0from std_srvs.srv import SetBool
    pub.publish(cmd)
    pub_motion.publish("BW")

def lt():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z = AngularVel.get()
    pub.publish(cmd)
    pub_motion.publish("LT")

def rt():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z = -AngularVel.get()
    pub.publish(cmd)
    pub_motion.publish("RT")
    
def set_pen_status(on):
    rospy.wait_for_service('/turtle1/set_pen')
    try:
        set_pen = rospy.ServiceProxy('/turtle1/set_pen', SetBool)
        response = set_pen(on)
        return response.success
    except rospy.ServiceException as e:
        print("Service call failed:", e)
        return False
        
        
LinearVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
LinearVel.set(1)  # 1 is default value for scale
LinearVel.pack()

AngularVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
AngularVel.set(1)  # 1 is default value for scale
AngularVel.pack()

B1 = Button(text="FW", command=fw)
B1.place(x=73, y=120)

B2 = Button(text="BW", command=bw)
B2.place(x=73, y=230)

B3 = Button(text="LT", command=lt)
B3.place(x=20, y=180)

B4 = Button(text="RT", command=rt)
B4.place(x=128, y=180)

frame.mainloop()

