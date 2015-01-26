
from detection.Detection import Detection
from detection.SquareDetection import SquareDetection
from detection.CircleDetection import CircleDetection
from Stepper import Stepper
from Driver import Driver

import time

#
# This script is controlling the main logic for the 
# autonomous robot decisions.
#

if __name__ == '__main__':

	# initialize Driver object for stepper motor controls
	d = Driver(0.003)

	# move a bit forwards (first feedback)
	for i in range(0,10):
		d.forwards()

	# this first initialization will also initialize the 
	# raspberry pi camera (will happen only once in this program)
	circleDetection = CircleDetection(draw=False,width=640 ,height= 480, debug=True)

	while(circleDetection.isRunning()):
		# does the detection and frame analysis
		(circle, frame) = circleDetection.loop()

		print("circle found: " + str(circle))
		# if no circle is shown, turn right (right hand rule)
		if circle==None:
			for i in range(0,60):
				d.rotateRight()
		# if a circle is visible on the right side, turn right
		elif circle[0] > 400:
			print("YAY!!! right direction")
			for i in range(0,5):
				d.rotateRight()
		# if a circle is visible on the left side, turn left
		elif circle[0] < 266:
			print("YAY!!! left direction")
			for i in range(0,5):
				d.rotateLeft()
		# if a circle is visible in the middle, move on
		else:
			print("YAY!!! straight direction")
			for i in range(0,100):
				d.forwards()
		# if a circle has a huge diameter, move on and stop circle detection
		if circle != None and circle[2] > 130:
			circleDetection.stop()
			for i in range(0,100):
				d.forwards()

	squareDetection = SquareDetection(draw=False, debug=True)

	while(squareDetection.isRunning()):
		# does the detection and frame analysis
		(square, frame) = squareDetection.loop()

		# if no frame is found turn right
		if len(square) == 0:
			print("square not found: "+str(square))
			for i in range(0,60):
				d.rotateRight()
		else:
			# calculate the avarage middle position of the square
			avrg = sum([x[0][0]/4 for x in square[0]])	
			print("square found: avrg x-position: "+ str(avrg))
			# if the position is more on the right, turn right 
			if(avrg > 360):
				print("YAY!!! right direction")
				for i in range(0,5):
					d.rotateRight()
			# if the position is more on the left, turn left
			elif(avrg < 280):
				print("YAY!!! left direction")
				for i in range(0,5):
					d.rotateLeft()
			# if the position is in the center, move forwards
			else:
				print("YAY!!! straight direction")
				for i in range(0,100):
					d.forwards()
	
