#!/usr/bin/env python3

from tkinter import*
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool
from std_msgs.msg import Float32
from std_srvs.srv import Trigger 
from sensor_msgs.msg import JointState
from math import pi
from PIL import Image, ImageTk


root  = Tk()
root.title("RR Robot remote")
root.geometry("900x400")

#canvas = Canvas(root ,width=900, height=400)
#canvas.pack()


# Load and resize the image
image = Image.open('Untitled.png').resize((900, 400))
photo_image = ImageTk.PhotoImage(image)

# Create a canvas and place the image
canvas = Canvas(root, width=900, height=400, bg='white')
canvas.create_image(0, 0, image=photo_image, anchor='nw')  # Place at top-left corner
canvas.pack()


class GUI:
	def __init__(self, canvas):
	
		# init general variable
		self.guiControlMode = True 
		self.canvas = canvas
		self.servo1_data = 0
		self.servo2_data = 0
		self.onStatus = False
		self.connected = False
		self.model_angle1 = 0
		self.model_angle2 = 0
				
		# init gui controller part เเก้ตั้งเเต่ตรงนี้`
		
		
		self.gui_label = Label(root, text="GUI Controller", font=("Arial", 16), fg="blue")
		self.gui_label.place(x= 85, y= 20)

		self.angle1 = Scale(root, from_=-90, to=90, orient=HORIZONTAL)
		self.angle1.set(0)
		self.angle1.place(x= 100, y=80)

		self.angle2 = Scale(root, from_=-90, to=90, orient=HORIZONTAL)
		self.angle2.set(0)
		self.angle2.place(x= 100, y=160)

		self.set_botton = Button(root, text = "set" , command = self.set_command)
		self.set_botton.place(x= 125, y=240)

		self.home_botton = Button(root, text = "home" , command = self.home_command)
		self.home_botton.place(x= 117, y=320)

		self.status1_label = Label(root, text="GUI controller's status:", font=("Arial", 12))
		self.status1_label.place(x= 60, y=370)

		self.status_light1 = self.canvas.create_oval(230, 373, 250, 393, fill='green')

		self.line1 = self.canvas.create_line(300, 0, 300, 450, fill='red', width=2)
		
		
		# init current status part
		
		self.current_label = Label(root, text="Current Position", font=("Arial", 16), fg="blue")
		self.current_label.place(x= 380, y= 20)


		self.change_mode_botton = Button(root, text = "change mode" , command = self.change_mode)
		self.change_mode_botton.place(x= 392, y=320)
		
		self.Angle1_label = Label(root, text="First servo's angle     :", font=("Arial", 13))
		self.Angle1_label.place(x=310, y= 100)
		
		self.Angle1_data = Label(root, text="No data", font=("Arial", 12), fg="red")
		self.Angle1_data.place(x=490, y= 100)
		
		self.Angle2_label = Label(root, text="Second servo's angle:", font=("Arial", 13))
		self.Angle2_label.place(x=310, y= 180)
		
		self.Angle2_data = Label(root, text="No data", font=("Arial", 12), fg="red")
		self.Angle2_data.place(x=490, y= 180)
		
		self.connection_label = Label(root, text = "Connection status: ")
		self.connection_label.place(x = 370, y = 370)
		
		
		self.status_light3 = self.canvas.create_oval(505, 373, 525, 393, fill='red') # not debug
		
		self.line2 = self.canvas.create_line(600, 0, 600 ,450, fill='red', width=2)

		
		# init potent controller part

		self.Poten_label = Label(root, text="Potentiometer controller", font=("Arial", 16), fg="blue")
		self.Poten_label.place(x= 640, y= 20)
		
		self.potent1_label = Label(root, text="First potentiometer's data     :", font=("Arial", 13))
		self.potent1_label.place(x=605, y= 100)
		
		self.potent1_data = Label(root, text="No data", font=("Arial", 12), fg="red")
		self.potent1_data.place(x=840, y= 100)
		
		self.potent2_label = Label(root, text="Second potentiometer's data:", font=("Arial", 13))
		self.potent2_label.place(x=605, y= 180)
		
		self.potent2_data = Label(root, text="No data", font=("Arial", 12), fg="red")
		self.potent2_data.place(x=840, y= 180)
		
		self.status_light2 = self.canvas.create_oval(840, 373, 860, 393, fill='red')
		self.status2_label = Label(root, text="Potentiometer's status:", font=("Arial", 12))
		self.status2_label.place(x= 660, y=370)
		
		# `เเก้เเค่ถึงตรงนี้

	
	# Buttons function
	
	def set_command(self):
		pass
			
		 
	def change_mode(self):
		pass
		
	def home_command(self):
		pass
			


gui = GUI(canvas)
root.mainloop()

